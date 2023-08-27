from microbit import *
import radio
import math
import music

def init():
    global count
    global on_off_switch
    count = 0
    on_off_switch = 9
    
def radio_config():
    radio.config(group=50, power=7)
    radio.on()

def send_message(message_send):
    radio.send(str(message_send))
    print("送信完了")

def recieve_and_send_message(message_send):
    radio.on()
    print("相手の年収を待っています…")
    while True:
        message = radio.receive()
        radio.send(str(message_send))
        sleep(500)
        if message:
            print(message)
            return int(message)

def salary_input(count):
    
    while not button_a.was_pressed() and button_b.was_pressed():
        sleep(100)  # Don't constantly poll the button, give a little delay to reduce power usage
    
    print('年収を入力してください。1ライト、100万円')
    print('')
    print('ロゴボタンをタッチで決定')
    print('')
    while True:
        if button_b.was_pressed():
            if count <= 4:
                display.set_pixel(count,0,9)
                count = count + 1
                print(str(int(count)) + "00万円")
            elif count >= 5 and count <= 9:
                display_count = count - 5
                display.set_pixel(display_count,1,9)
                count = count + 1
                print(str(int(count)) + "00万円")
            elif count >= 10 and count <= 14:
                display_count = count - 10
                display.set_pixel(display_count,2,9)
                count = count + 1
                print(str(int(count)) + "00万円")
            elif count >= 15 and count <= 19:
                display_count = count - 15
                display.set_pixel(display_count,3,9)
                count = count + 1
                print(str(int(count)) + "00万円")
            elif count >= 20 and count <= 24:
                display_count = count - 20
                display.set_pixel(display_count,4,9)
                count = count + 1
                print(str(int(count)) + "00万円")
                
        elif button_a.was_pressed():
            if count >= 1 and count <= 5:
                count_display = count - 1
                display.set_pixel(count_display,0,0)
                count = count - 1
                print(str(int(count)) + "00万円")
            elif count >= 6 and count <= 10:
                count_display = count - 1 - 5
                display.set_pixel(count_display,1,0)
                count = count - 1
                print(str(int(count)) + "00万円")
            elif count >= 11 and count <= 15:
                count_display = count - 1 - 10
                display.set_pixel(count_display,2,0)
                count = count - 1
                print(str(int(count)) + "00万円")
            elif count >= 16 and count <= 20:
                count_display = count - 1 - 15
                display.set_pixel(count_display,3,0)
                count = count - 1
                print(str(int(count)) + "00万円")
            elif count >= 21 and count <= 25:
                count_display = count - 1 - 20
                display.set_pixel(count_display,4,0)
                count = count - 1
                print(str(int(count)) + "00万円")
            elif count <= 0:
                pass
        elif pin_logo.is_touched():
            print('あなたの年収は' + str(int(count)) + '00万円で決定！')
            break
    sleep(1000)
    display.show(Image.HAPPY)
    return count * 100

def calculate_difference(salary, salary_recieved):
    difference = salary_recieved - salary
    print("給料差は" + str(difference))
    return difference

def calculate_desired_angle(salary_difference):
    if salary_difference > 0: 
        # if the salary difference is positive, meaning your salary is lower, calculate bend angle accordingly
        if salary_difference > 0 and salary_difference <= 500:
            bend_angle = 20
            print("お辞儀しなきゃいけない角度は" + str(bend_angle) + "°")
            return bend_angle
        elif salary_difference > 500 and salary_difference <= 1000:
            bend_angle = 40
            print("お辞儀しなきゃいけない角度は" + str(bend_angle) + "°")
            return bend_angle
        elif salary_difference > 1000 and salary_difference <= 1500:
            bend_angle = 60
            print("お辞儀しなきゃいけない角度は" + str(bend_angle) + "°")
            return bend_angle
        elif salary_difference > 1500 and salary_difference <= 2000:
            bend_angle = 80
            print("お辞儀しなきゃいけない角度は" + str(bend_angle) + "°")
            return bend_angle
        elif salary_difference > 2000:
            bend_angle = 100
            print("お辞儀しなきゃいけない角度は" + str(bend_angle) + "°")
            return bend_angle
    else:
        #Only bend a certain angle like 10 deg because your salary is heigher
        bend_angle = 20
        print("お辞儀しなきゃいけない角度は" + str(bend_angle) + "°")
        return bend_angle
        
def measure_accel(bend_angle):
    print('Starting Acceleration Measurement...')
    sleep(2000)
        
    while True:  
        x_strength = accelerometer.get_x()
        y_strength = accelerometer.get_y()
        z_strength = accelerometer.get_z()
        angle_rad = math.atan2(z_strength, y_strength)
        angle_deg = math.degrees(angle_rad)  # Convert the result from radians to degrees
        print("今の角度は" + str(angle_deg) + "°")
        if angle_deg <= (bend_angle/5)*1:
            display.show(Image('00000:'
                               '00000:'
                               '00000:'
                               '00000:'
                               '00000'))
            music.stop()
        elif angle_deg <= (bend_angle/5)*2:
            display.show(Image('99999:'
                               '00000:'
                               '00000:'
                               '00000:'
                               '00000'))
            music.stop()
        elif angle_deg <= (bend_angle/5)*3:
            display.show(Image('99999:'
                               '99999:'
                               '00000:'
                               '00000:'
                               '00000'))
            music.stop()
        elif angle_deg <= (bend_angle/5)*4:
            display.show(Image('99999:'
                               '99999:'
                               '99999:'
                               '00000:'
                               '00000'))
            music.stop()
        elif angle_deg <= (bend_angle/5)*5:
            display.show(Image('99999:'
                               '99999:'
                               '99999:'
                               '99999:'
                               '00000'))
            music.stop()
            
        elif angle_deg <= (bend_angle/5)*6:
            display.show(Image('99999:'
                               '99999:'
                               '99999:'
                               '99999:'
                               '99999'))
            music.pitch(460)
        
        # print("X_Aceel: " + str(x_strength) + " " + "Y_Aceel: " + str(y_strength) + " "  + "Z_Aceel: " + str(z_strength) + " " )
        sleep(50)
    
        if pin_logo.is_touched():
            break



init()
radio_config()

salary = salary_input(count)

salary_recieved = recieve_and_send_message(salary)
salary_difference = calculate_difference(salary, salary_recieved)
bend_angle=calculate_desired_angle(salary_difference)

measure_accel(bend_angle)

