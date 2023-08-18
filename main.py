from random import random
from flask import flash, Flask, request, render_template, redirect, session, jsonify
import mysql.connector
import pyaes,pbkdf2,secrets
import os
import string
import random
import hashlib
import json


conn = mysql.connector.connect(host="localhost", user="root", password="manoj", database="healthmonitoring", charset="utf8")
cursor = conn.cursor()
app = Flask(__name__)
app.secret_key = os.urandom(24)


#_________________________________________________________________________________
#_____________________________Index Pgae__________________________________________
#_________________________________________________________________________________

@app.route('/')
def index():
    return render_template("index.html")

# _________________________admin login page_______________________________________
@app.route('/admin')
def admin():
    return render_template("admin.html")

# _________________________Admin_Login_backend page_______________________________


@app.route('/Adminlogin', methods=['POST'])
def Adminlogin():
    name = request.form.get('name')
    pswd = request.form.get('pswd')
    d = 0
    cursor.execute("""select * from `adminlogin` where ausername like '{}' and apassword like '{}'""".format(name, pswd))
    admin = cursor.fetchall()
    print(admin)
    if len(admin) > 0:
        d = 1
        session['user_id'] = admin[0][0]
        print(session['user_id'])

        #return redirect('/adminhome')
    else:
        d = 0
        #return redirect('/')

    return jsonify(d)

# _________________________Admin_Home page________________________________________

@app.route('/adminhome')
def adminhome():
    return render_template("admin/adminhome.html")

# _________________________Admin_Add hospital page_______________________________

@app.route('/addhospital')
def addhospital():
    return render_template("admin/addhospital.html")


# _________________________Admin_Adding hospital page_______________________________

@app.route('/Adding_hospital', methods=['POST'])
def Adding_hospital():
    hname = request.form.get('hname')
    hadrrs = request.form.get('hadrrs')
    city = request.form.get('city')
    state = request.form.get('state')
    zcode = request.form.get('zcode')
    country = request.form.get('country')
    hphone = request.form.get('hphone')
    hemail = request.form.get('hemail')


    cursor.execute("""INSERT INTO `hospital`(`hospitalname`,`hospitaladdrs`,`hcity`,`hstate`,`hzcode`,`hcountry`,`hphone`, `hemail`) VALUES ('{}','{}','{}','{}',
    '{}','{}','{}','{}')""".format(hname,hadrrs, city,  state, zcode, country,hphone,hemail))
    conn.commit()
    return render_template("admin/addhospital.html")

# _________________________Admin_View_Hospital page____________________________________

@app.route('/viewhospital')
def viewhospital():
    cursor.execute("""SELECT * FROM `hospital`""")
    hospital = cursor.fetchall()
    return render_template("admin/viewhospital.html",data=hospital)

# _________________________Admin_delete_Hospital_page_______________________________

@app.route('/delete_hospital/<string:id_data>/', methods=['POST', 'GET'])
def delete_hospital(id_data):
    cursor.execute("DELETE FROM `hospital` WHERE  hid = %s", (id_data,))
    conn.commit()
    return redirect('/viewhospital')

# # _________________________Admin_Add Doctor page_______________________________

@app.route('/adddoctor')
def adddoctor():
    cursor4 = conn.cursor()
    cursor4.execute("""select hid,hospitalname from `hospital`""")
    h = cursor4.fetchall()
    print(h)
    return render_template("admin/adddoctor.html", dataa=h)

# _________________________Admin Adding doctors page____________________________________

@app.route('/Adding_doctor', methods=['POST'])
def Adding_doctor():
    dname = request.form.get('dname')
    dadrrs = request.form.get('dadrrs')
    dphone = request.form.get('dphone')
    Specialistin = request.form.get('Specialistin')
    demail = request.form.get('demail')
    dpswrd = request.form.get('dpswrd')
    ahn = request.form.get('ahn')
    res = 0
    cursor.execute("""select * from `doctor` where doctoremail like '{}'""".format(demail))
    admin = cursor.fetchall()
    print(admin)
    if len(admin) > 0:
        res = 0
    else:
        res = 1
    cursor.execute("""INSERT INTO `doctor`(`doctorname`,`doctoraddrs`,`doctorphone`,`SpecialistIn`,`doctoremail`,`dpasswrd`,`hospitalname`) VALUES ('{}','{}','{}','{}','{}','{}','{}'
    )""".format(dname, dadrrs, dphone, Specialistin, demail, dpswrd, ahn))
    conn.commit()

    return jsonify(res)

# _________________________Admin View_doctors page_______________________________

@app.route('/viewdoctor')
def viewdoctor():

    cursor.execute("""SELECT  d.*, h1.hospitalname FROM `doctor` AS d JOIN hospital AS h1 ON h1.hid = d.hospitalname""")
    doctor = cursor.fetchall()
    print(doctor)
    #array = []
    #print(doctor)
    #for i in doctor:
        #hashed_string = hashlib.sha256(doctor[0][1].encode('utf-8')).hexdigest()
        #array.append({"no": doctor[0][0],"name": hashed_string,"address": doctor[0][2],"pho": doctor[0][3],"specialised": doctor[0][4],"email": doctor[0][5],"password": doctor[0][6],"hospital": doctor[0][7]})

    #print(array)
    return render_template("admin/viewdoctor.html", data=doctor)


# _________________________Admin delete_Doctor_page_______________________________

@app.route('/delete_doctor/<string:id_data>/', methods=['POST', 'GET'])
def delete_doctor(id_data):
    cursor.execute("DELETE FROM `doctor` WHERE  did = %s", (id_data,))
    conn.commit()
    return redirect('/viewdoctor')

#---------------------------Admin Patient------------------------------

@app.route('/adminpatient')
def adminpatient():
    return render_template("admin/patient.html")

# _________________________Admin Patient view page______________________________
@app.route('/adminnviewpatient')
def adminnviewpatient():
        #print("hi")
        cursor.execute("""SELECT `pid`,CAST(AES_DECRYPT(`pname`, `pkey`) AS CHAR) AS pname,CAST(AES_DECRYPT(`pemail`, `pkey`) AS CHAR) AS pemail,`page`,`pgender`,CAST(AES_DECRYPT(`pcontact`, `pkey`) AS CHAR) AS `pcontact` FROM patient""")
        patient2 = cursor.fetchall()
        print(patient2)
        return render_template("admin/patient.html", data=patient2)

#-------------------------Admin add Patient--------------------
@app.route('/adminaddpatientspage')
def adminaddpatientspage():
    return render_template("admin/addpatient.html")

#----------------------Admin Adding Patients-------------------------

@app.route('/adminaddpatients', methods=['POST'])
def adminaddpatients():
    pname = request.form.get('pname')
    pemail = request.form.get('pemail')
    page = request.form.get('page')
    select = request.form.get('select')
    pcontact = request.form.get('pcontact')
    Password = request.form.get('Password')


    password = "s3cr3t*c0d3"
    passwordSalt = os.urandom(16)
    key = pbkdf2.PBKDF2(password, passwordSalt).read(32)

    iv = secrets.randbits(256)
    name = f'{pname}'
    email = f'{pemail}'
    age = f'{page}'
    gender = f'{select}'
    contact = f'{pcontact}'
    password = f'{Password}'


    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    pname = aes.encrypt(name)
    pemail = aes.encrypt(email)
    page = aes.encrypt(age)
    select = aes.encrypt(gender)
    pcontact = aes.encrypt(contact)
    Password = aes.encrypt(password)

    N = 7

    key = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
    print(key)
    cursor.execute("""INSERT INTO `patient`(`pname`,`pemail`,`page`,`pgender`,`pcontact`,`pkey`,`password`) VALUES (AES_ENCRYPT('{}','{}'),AES_ENCRYPT('{}','{}'),'{}','{}',AES_ENCRYPT('{}','{}'),'{}','{}')""".format(
            pname, key, pemail, key, page, select, pcontact, key, key, Password))
    conn.commit()


    return redirect('/adminnviewpatient')


#-------------------------Admin Medicaldetails Page-------------------------------------------

@app.route('/adminAddingmedicaldetailpage')
def adminAddingmedicaldetailpage():
    cursor9 = conn.cursor()
    cursor9.execute("""select hid,hospitalname from `hospital`""")
    hospital1 = cursor9.fetchall()
    print(hospital1)
    cursor10 = conn.cursor()
    cursor10.execute("""select did,doctorname from `doctor`""")
    doctor1 = cursor10.fetchall()
    print(doctor1)
    return render_template("admin/addmedicaldetails.html", datahos=hospital1, datadoc=doctor1)





#------------------------------Admin ADD Medicaldetails Page--------------------------------------

@app.route('/adminAddingmedicaldetail', methods=['POST'])
def adminAddingmedicaldetail():
    pid = request.form.get('pid')
    bp = request.form.get('bp')
    hr = request.form.get('hr')
    bg = request.form.get('bg')
    tem = request.form.get('tem')
    hissue = request.form.get('hissue')
    rmedical = request.form.get('rmedical')
    dname = request.form.get('dname')
    hn = request.form.get('hn')

    print(rmedical)
    #a_string = 'this string holds important and private information'
    encodedresponsedata = hashlib.sha256(rmedical.encode('utf-8')).hexdigest()
    print(encodedresponsedata)

    cursor.execute("""INSERT INTO `patientmedicaldetails`(`pid`,`bp`,`heartrate`,`bloodgruop`,`temperature`,`healthissue`,`responsetomedication`,`doctorname`,`hospitalname`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}'
    )""".format(pid, bp, hr, bg, tem, hissue, encodedresponsedata, dname, hn))
    conn.commit()
    return redirect("/adminnviewpatient")

#----------------------------Admin View Medicaldetails Page-----------------------------------------

@app.route('/adminmedicaldetails', methods=['POST'])
def adminmedicaldetails():
    pid = request.form.get('pid')
    print(pid)
    cursor.execute("""SELECT P.*, h1.hospitalname, D.`doctorname` FROM `patientmedicaldetails` AS P JOIN hospital AS h1 ON h1.hid = P.hospitalname JOIN `doctor` AS D ON D.did = P.doctorname WHERE pid like '{}'""".format(pid))
    medical = cursor.fetchall()
    print(medical)
    print("aaaaa")
    return jsonify(medical)

#---------------------------------------------------------------------
# _________________________Doctor page_______________________________
#---------------------------------------------------------------------

@app.route('/doctor')
def doctor():
    return render_template("/doctor.html")

# _________________________Doctor login_______________________________
@app.route('/doctorlogin', methods=['POST'])
def doctorlogin():
    flash("Doctor Logedin Successfully")
    demail = request.form.get('demail')
    dpswd = request.form.get('dpswd')
    d = 0
    cursor.execute("""select * from `doctor` where doctoremail like '{}' and dpasswrd like '{}'""".format(demail, dpswd))
    doctor = cursor.fetchall()
    print(doctor)
    if len(doctor) > 0:
        session['doctor_id'] = doctor[0][0]
        d = 1
        #return redirect('/doctorhome')
    else:
        d = 0
        #return redirect('/')

    return jsonify(d)


# _________________________Doctor page_________________________________________

@app.route('/doctorhome')
def doctorhome():
    return render_template("doctor/doctorhome.html")

# _________________________Doctor Patient page_______________________________

@app.route('/patient')
def patient():
    return render_template("doctor/patient.html")


# _________________________Doctor Patient view page______________________________

@app.route('/viewpatient')
def viewpatient():

    cursor.execute("""SELECT `pid`,CAST(AES_DECRYPT(`pname`, `pkey`) AS CHAR) AS pname,CAST(AES_DECRYPT(`pemail`, `pkey`) AS CHAR) AS pemail,`page`,`pgender`,CAST(AES_DECRYPT(`pcontact`, `pkey`) AS CHAR) AS `pcontact` FROM patient""")
    patient = cursor.fetchall()
    print(patient)
    return render_template("doctor/patient.html", data=patient)
#----------------------------Doctor ADD patient Page----------------------------------------

@app.route('/addpatientspage')
def addpatientspage():
    return render_template("doctor/addpatient.html")
#------------------------------Doctor Adding Medical Details Page --------------------------------------

@app.route('/Addingmedicaldetailpage')
def Addingmedicaldetailpage():
    cursor.execute("""select hid,hospitalname from `hospital`""")
    hospital = cursor.fetchall()
    cursor1 = conn.cursor()
    cursor1.execute("""select did,doctorname from `doctor`""")
    doctor = cursor1.fetchall()
    return render_template("doctor/addmedicaldetails.html", data=hospital,data1=doctor)

#---------------------------Doctor Adding Medical Details  Page -----------------------------------------

@app.route('/Addingmedicaldetail', methods=['POST'])
def Addingmedicaldetail():
    pid = request.form.get('pid')
    bp = request.form.get('bp')
    hr = request.form.get('hr')
    bg = request.form.get('bg')
    tem = request.form.get('tem')
    hissue = request.form.get('hissue')
    rmedical = request.form.get('rmedical')
    dname = request.form.get('dname')
    hospital = request.form.get('hospital')

    encodedresponsedata = hashlib.sha256(rmedical.encode('utf-8')).hexdigest()
    print(encodedresponsedata)

    decrypted = decrypt(encodedresponsedata)

    print(decrypted)


    cursor.execute("""INSERT INTO `patientmedicaldetails`(`pid`,`bp`,`heartrate`,`bloodgruop`,`temperature`,`healthissue`,`responsetomedication`,`doctorname`,`hospitalname`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}'
    )""".format(pid, bp, hr, bg, tem, hissue, encodedresponsedata, dname, hospital))
    conn.commit()
    return redirect("/viewpatient")


# _________________________Doctor AddPatients page___________________________

@app.route('/addpatients', methods=['POST'])
def addpatients():
    pname = request.form.get('pname')
    pemail = request.form.get('pemail')
    page = request.form.get('page')
    select = request.form.get('select')
    pcontact = request.form.get('pcontact')
    Password = request.form.get('Password')


    password = "s3cr3t*c0d3"
    passwordSalt = os.urandom(16)
    key = pbkdf2.PBKDF2(password, passwordSalt).read(32)

    iv = secrets.randbits(256)
    plaintext = f'{pname}'
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(plaintext)
    print(ciphertext)

    N = 7

    key = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
    print(key)

    cursor.execute("""INSERT INTO `patient`(`pname`,`pemail`,`page`,`pgender`,`pcontact`,`pkey`,`password`) VALUES (AES_ENCRYPT('{}','{}'),AES_ENCRYPT('{}','{}'),'{}','{}',AES_ENCRYPT('{}','{}'),'{}','{}')""".format(pname,key,pemail,key,page,select,pcontact,key,key,Password))
    conn.commit()

    return redirect('/viewpatient')


#-------------------------------doctor medical details page--------------------------------------------
@app.route('/medical')
def medical():
    return render_template("doctor/medicaldetails.html")
# _________________________doctor view medical details_______________________________

@app.route('/medicaldetails1', methods=['POST'])
def medicaldetails1():
    pid = request.form.get('pid')
    print(pid)
    cursor.execute("""SELECT P.*, h1.hospitalname, D.`doctorname` FROM `patientmedicaldetails` AS P JOIN hospital AS h1 ON h1.hid = P.hospitalname JOIN `doctor` AS D ON D.did = P.doctorname WHERE pid like '{}'""".format(pid))
    medical = cursor.fetchall()
    print(medical)
    print("aaaaa")
    return jsonify(medical)

#____________________________________________________________________
# _________________________User page_________________________________
#____________________________________________________________________


@app.route('/user')
def user():
    return render_template("user.html")

# _________________________User login_______________________________
@app.route('/userlogin', methods=['POST'])
def userlogin():
    uemail = request.form.get('uemail')
    upswd = request.form.get('upswd')
    pkey = request.form.get('upswd')
    p=0
    print(upswd)
    cursor.execute("""select * from `patient` where `password` like '{}'""".format(upswd))
    user = cursor.fetchall()
    print(user)
    if len(user) > 0:
        key = user[0][6]
        print(user[0][6])
        cursor.execute("select * from `patient` where CAST(AES_DECRYPT(`pemail`, `pkey`) AS CHAR) like '{}'".format(uemail))
        user2 = cursor.fetchall()
        if len(user2) > 0:
            session['user_id'] = user2[0][0]
            p = 1
        #return redirect('/userhome')
    else:
            p = 0
        #return redirect('/')
    return jsonify(p)


# _________________________User home page_______________________________

@app.route('/userhome')
def userhome():
    return render_template("patient/patienthomepage.html")


#-------------------------View Medical details_____________________________

@app.route('/viewmedicaldetails')
def viewmedicaldetails():
    return render_template("patient/viewmedicaldetails.html")

#---------------------------------View Medical details------------------------------------------

@app.route('/viewmedicaldetails2', methods=['POST'])
def viewmedicaldetails2():
    Username1 = session['user_id']
    #cursor.execute("""SELECT P.*, h1.hospitalname, D.`doctorname` FROM `patientmedicaldetails` AS P JOIN hospital AS h1 ON h1.hid = P.hospitalname JOIN `doctor` AS D ON D.did = P.doctorname WHERE pid like '{}'""".format( Username1))

    cursor.execute("""SELECT P.*, CAST(AES_DECRYPT(`responsetomedication`, `pkey`) AS CHAR) AS responsetomedication, h1.hospitalname, D.`doctorname` FROM `patientmedicaldetails` AS P JOIN hospital AS h1 ON h1.hid = P.hospitalname JOIN `doctor` AS D ON D.did = P.doctorname WHERE pid like '{}'""".format(Username1))
    #("""SELECT `pid`,CAST(AES_DECRYPT(`pname`, `pkey`) AS CHAR) AS pname,CAST(AES_DECRYPT(`pemail`, `pkey`) AS CHAR) AS pemail,`page`,`pgender`,CAST(AES_DECRYPT(`pcontact`, `pkey`) AS CHAR) AS `pcontact` FROM patient""")
    medical = cursor.fetchall()
    my_list = []
    for row in medical:
        x = {
        "slno": row[0],
        "bp": row[2],
        "heartrate": row[3],
        "bloodgruop":row[4],
        "temperature" :row[5],
        "healthissue":row[6],
        "responsetomedication":row[7],
        "doctorname":row[11],
        "hospitalname":row[10]
             }
        y = json.dumps(x)
        my_list.append(y)
        print(my_list)
    return jsonify(my_list)


#--------------------------View Medical detail_______________________________________

@app.route('/viewmedicaldetails1')
def viewmedicaldetails1():
    return render_template("patient/viewmedicaldetails1.html")

#--------------------------------------------------------------------------------------
#________________________________******END*****________________________________________
#--------------------------------------------------------------------------------------



if __name__ == "__main__":
    app.run(debug=True)