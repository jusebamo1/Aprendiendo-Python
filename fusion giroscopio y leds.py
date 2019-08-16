#FUSION CODIGOS LEDS Y GIROSCOPIO ························

import smbus            #import SMBus module of I2C
from time import sleep          #import
import time as t
import RPi.GPIO as GPIO

'''
Variables para el giroscopio
'''
#------------------------------------------------------------------------
#Some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

'''
Variable para leds
'''
#Variables de pines
entrada1 = 15
led1=  11
led2=  12
led3=  13
led4=  15
led5=  16

#SetUp Variables leds o configuraciones
#-------------------------------------------------------

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(entrada1, GPIO.IN)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(led5, GPIO.OUT)


def MPU_Init():
    #write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
    
    #Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    
    #Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)
    
    #Write to Gyro configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    
    #Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    #Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value
    
bus = smbus.SMBus(1)    # or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

print (" Reading Data of Gyroscope and Accelerometer")

#VALORES DE GIRO Y ACELERACION

valX = []
valY = []
valZ = []
try:
    while True:
        
        #Read Accelerometer raw value
        acc_x = read_raw_data(ACCEL_XOUT_H)
        acc_y = read_raw_data(ACCEL_YOUT_H)
        acc_z = read_raw_data(ACCEL_ZOUT_H)
        
        #Read Gyroscope raw value
        gyro_x = read_raw_data(GYRO_XOUT_H)
        gyro_y = read_raw_data(GYRO_YOUT_H)
        gyro_z = read_raw_data(GYRO_ZOUT_H)
        
        #Full scale range +/- 250 degree/C as per sensitivity scale factor
        Ax = acc_x/16384.0
        Ay = acc_y/16384.0
        Az = acc_z/16384.0
        
        Gx = gyro_x/131.0
        Gy = gyro_y/131.0
        Gz = gyro_z/131.0
        
        valX.append(Ax)
        valY.append(Ay)
        valZ.append(Az)
        
        sleep(1)
        
        '''print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s",
               "\tGy=%.2f" %Gy, u'\u00b0'+ "/s",
               "\tGz=%.2f" %Gz, u'\u00b0'+ "/s",
               "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay,
               "\tAz=%.2f g" %Az)
        #VAL.append[Gx,Gy,Gz]
        sleep(1)
        '''
        if Ax >= 0.13 and Ay >= -0.1 and Az >= -0.92 :
            
            GPIO.output(led3,GPIO.HIGH)
            t.sleep(0.1)
            



        elif Ax >= -0.04 and Ay >= -0.56 and Az >= -0.04:
            GPIO.output(led4,GPIO.HIGH)
            t.sleep(0.1)
            
            GPIO.output(led4,GPIO.LOW)
            t.sleep(0.1)
            
            GPIO.output(led5,GPIO.HIGH)
            t.sleep(0.1)
            
            GPIO.output(led5,GPIO.LOW)
            t.sleep(0.1)
            
        else:
            
            
            GPIO.output(led2,GPIO.HIGH)
            t.sleep(0.1)
            
            GPIO.output(led2,GPIO.LOW)
            t.sleep(0.1)
            
            GPIO.output(led1,GPIO.HIGH)
            t.sleep(0.1)
            
            GPIO.output(led1,GPIO.LOW)
            t.sleep(0.1)
            
        
            
        
    
        
except KeyboardInterrupt:
    pass

finally:
    print("Acabé")
    

GPIO.cleanup()