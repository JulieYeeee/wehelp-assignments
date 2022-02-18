
from flask import Flask,jsonify,json
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
import mysql.connector



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="test1234",
  database="website"
)


mycursor = mydb.cursor(buffered=True)#連線資料庫
app=Flask(__name__) #建立Flask物件
app.secret_key="asdfghjkl" #session密鑰




@app.route("/api/members",methods=["GET"])
def memberData():
    username=request.args.get("username")
    sql="SELECT id,name,username FROM member WHERE username=%s"
    val=(username,)
    mycursor.execute(sql,val)
    result=mycursor.fetchone()
    if result!=None:
        data={"id":result[0],"name":result[1],"username":result[2]}
        return jsonify({"data":data})
    else:
        return jsonify({"data":None})


@app.route("/",methods=["get"])
def memberIndex():
    return render_template("index.html")


@app.route("/signup",methods=["POST"]) 
def signup():
    rgName=request.form["rgName"]
    rgAccount=request.form["rgAccount"]
    rgPassword=request.form["rgPassword"]
    sql="SELECT username FROM member WHERE username=%s"
    val=(rgAccount,)
    mycursor.execute(sql,val)
    match=mycursor.fetchall()
    if match!=[]:
       return redirect("/error?warning=帳號已被註冊_請登入或重新註冊")
    else:
        sql="INSERT INTO member(name,username,password) VALUES(%s,%s,%s)"
        val=(rgName,rgAccount,rgPassword)
        mycursor.execute(sql,val)
        mydb.commit()
        return redirect(url_for("memberIndex"))
     
        

@app.route("/signin",methods=["post"])
def signin():
    signinAccount=request.form["signinAccount"]   #抓取網址上帳號資訊
    signinPassword =request.form["signinPassword"]  #抓取網址上密碼資訊
    sql="SELECT id FROM member WHERE username=%s"   #以下先確認抓取的帳號資訊室否資料庫中有吻合資料若有就抓ID
    val=(signinAccount,)
    mycursor.execute(sql,val)
    match=mycursor.fetchall()
    if match!=[]:  #若資料庫有抓到符合資料,那結果match不會是空列表,並接續抓密碼是否吻合
         sql="SELECT password FROM member WHERE id=%s"
         val=(match[0][0],)
         mycursor.execute(sql,val)
         pswMatch=mycursor.fetchall()
         if signinPassword==pswMatch[0][0]: #若密碼與資料庫內紀錄相符就redirect到登入成功頁
             sql="SELECT name FROM member WHERE id=%s"
             val=(match[0][0],)
             mycursor.execute(sql,val)
             name=mycursor.fetchall()
             session["name"]=name[0][0]
             return redirect(url_for("success"))
         else:
             return redirect("/error?warning=帳號或密碼錯誤") 
    else:
        return redirect("/error?warning=帳號或密碼錯誤")              
              


@app.route("/error",methods=["get"])
def error():
    warning=request.args.get("warning")
    return render_template("error.html",wrongMSG=warning)

@app.route("/member",methods=["get"])
def success():
    if session.get("name")!=None:
        name=session["name"]
        return render_template("success.html",會員名稱=name)
    else:
        return redirect(url_for("memberIndex"))
        

@app.route("/signout")
def signout():
    session.pop("name",None)
    return render_template("signout.html")



if __name__ == "__main__": #當此為主程式時就執行
    app.debug=True     #當程式碼有修改自動更新
    app.run(port=3000)  #在port3000執行