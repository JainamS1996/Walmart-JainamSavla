from flask import Flask,jsonify
import os,time,socket,getpass,platform,datetime, shutil 

app = Flask(__name__)

startTime = time.time()

#Reading the version of the application from the file
def get_current_version():
    file = open('app_version.txt','r')
    return file.readlines()[0].split(':')[1].strip()

#For Displaying the Up time
def get_uptime():
    return int(time.time() - startTime)


def disk_usage():
    path = "/app"
    stat = shutil.disk_usage(path) 
    return (stat[0]/10**9,stat[1]/10**9,stat[2]/10**9)

@app.route('/')
@app.route('/home/')
def home():
    #Logging the application
    app.logger.info('Home Page Request') 

    return "Hello !"

@app.route('/healthz/')
def health():
    #Logging the application
    app.logger.info('Health Check Request') 

    health={
           
            "Status" : "Success",
            "Version" : get_current_version(),
            "Uptime on " : "up since %s %s"% (datetime.datetime.today().strftime('%Y-%m-%d'), str(datetime.timedelta(seconds=get_uptime()))),
            "CurDir": os.getcwd(),
            "HostName": socket.gethostname(),
            "User": getpass.getuser(),
            "Disk Utilization(Total/Used/Free) " : disk_usage()
    }
            
    
    return jsonify(health)

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=80)
