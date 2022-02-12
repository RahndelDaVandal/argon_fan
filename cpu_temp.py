# cpu_temp.py
def get_temp() -> float:
    try:
        tempfp = open("/sys/class/thermal/thermal_zone0/temp", "r")
        temp = tempfp.readline()
        tempfp.close()
        val = float(int(temp)/1000)
    except IOError:
        val = 0
        #return val
        print(f'{val:.2f} c')
