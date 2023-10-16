from microbit import *
import radio
import math
import music


def init():
    global on_off_switch
    on_off_switch = 9


def radio_config():
    radio.config(group=50, power=7)
    radio.on()


def exchange_salaries(my_salary):
    radio.on()
    print("相手の年収を待っています…")
    while True:
        partner_salary = radio.receive()
        radio.send(str(my_salary))
        sleep(500)
        if partner_salary:
            print(partner_salary)
            return int(partner_salary)


def get_my_salary():
    count = 0
    while not button_a.was_pressed() and button_b.was_pressed():
        """
        Don't constantly poll the button, give a little delay
        to reduce power usage
        """
        sleep(100)

    print("年収を入力してください。1ライト、100万円\n\n")
    print("ロゴボタンをタッチで決定\n\n")
    while True:
        if button_b.was_pressed():
            count += 1
            display_salary_inputed(count, 9)
        elif button_a.was_pressed():
            if count == 0:
                continue
            count -= 1
            display_salary_inputed(count, 0)
        elif pin_logo.is_touched():
            print("あなたの年収は" + str(int(count)) + "00万円で決定!")
            break
    sleep(1000)
    display.show(Image.HAPPY)
    my_salary = count * 100
    return my_salary


def display_salary_inputed(count, brightness):
    print(str(int(count)) + "00万円")
    if brightness == 0:
        count += 1
    column = (count - 1) % 5
    row = (count - 1) // 5
    display.set_pixel(column, row, brightness)


def get_salary_difference(my_salary, partner_salary):
    difference = partner_salary - my_salary
    print("給料差は" + str(difference))
    return difference


def get_required_bow_angle(salary_difference):
    if salary_difference > 0:
        """
        if the salary difference is positive, meaning your salary is lower,
        calculate bend angle accordingly
        """
        required_bow_angle = 20 * ((salary_difference // 500) + 1)
        if required_bow_angle >= 100:
            required_bow_angle = 100
    else:
        # Only bend a certain angle like 10 deg because your salary is higher
        required_bow_angle = 20
    print("お辞儀しなきゃいけない角度は" + str(required_bow_angle) + "°")
    return required_bow_angle


def verify_bow_angle(required_bow_angle):
    print("Starting Acceleration Measurement...")
    sleep(2000)

    while True:
        y_strength = accelerometer.get_y()
        z_strength = accelerometer.get_z()
        angle_rad = math.atan2(z_strength, y_strength)
        # Convert the result from radians to degrees
        detected_bow_angle = math.degrees(angle_rad)
        print("今の角度は" + str(detected_bow_angle) + "°")

        angle_meter = 0
        if detected_bow_angle > 0:
            angle_meter = required_bow_angle // detected_bow_angle
        if angle_meter >= 5:
            angle_meter = 5

        angle_meter_image = ''
        for i in range(angle_meter):
            angle_meter_image += "99999:"
            i += 1
        for i in range(5 - angle_meter):
            angle_meter_image += "00000:"
            i += 1
        angle_meter_image = angle_meter_image[:-1]
        display.show(Image(angle_meter_image))

        if detected_bow_angle < required_bow_angle:
            music.stop()
        else:
            music.pitch(460)

        sleep(50)

        if pin_logo.is_touched():
            break


init()
radio_config()

my_salary = get_my_salary()

partner_salary = exchange_salaries(my_salary)
salary_difference = get_salary_difference(my_salary, partner_salary)
required_bow_angle = get_required_bow_angle(salary_difference)

verify_bow_angle(required_bow_angle)
