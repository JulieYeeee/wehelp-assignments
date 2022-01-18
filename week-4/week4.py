#載入會使用到的套件與功能
from email import message
from flask import Flask 
from flask import request
from flask import redirect
from flask import render_template
from flask import session


#建立application物件
app=Flask(__name__)
app.secret_key="a1a1a2s3a5s3a5s3ax5s"  #session需要的密鑰，可為隨機字串

#設定各種路徑與回應函式
#登入頁回應函式
@app.route("/")
def showIndex():
    return render_template("templates/index.html")

#登入帳密的回應函式，以POST方式處理可避免表單輸入資料顯露於網址中
@app.route("/signin",methods=["POST"])   
def login():
    account=request.form["account"]  #抓取要求字串中的帳號資料
    password=request.form["password"] #抓取要求字串中的密碼資料
    strAccount=str(account)  #字串化
    strPassword=str(password) #字串化
    #判斷輸入帳密是否正確
    if strAccount == "test":
        if strPassword == "test":
            session["account"]=strAccount #將使用者資料存入session
            return redirect("/member")#帳密皆符合導至會員頁
        elif strPassword=="":
            return redirect("/error?message=請輸入密碼")
        else:
            return redirect("/error?message=帳號或密碼錯誤")    
    elif strAccount=="":
        return redirect("/error?message=請輸入帳號")            
    else:
        return redirect("/error?message=帳號或密碼錯誤")
#登入成功頁面回應函式
@app.route("/member")
def showSuccess():
    if session.get("account")!=None: #判斷登入資料是否存在，若有存在就成功導入會員頁
        userName=session["account"]
        return render_template("templates/member.html",name=userName)
    else:
        return redirect("/") #若不存在導回首頁
#登出頁面回應函式
@app.route("/signout")
def logout():
    if session.get("account")!=None:
        session.pop("account",None)#每當登出就執行Key為account的欄位資料刪除
        return render_template("templates/signout.html")
    else:
        return redirect("/")#若不存導回首頁
#帳密登入錯誤回應函式
@app.route("/error")
def showFalse():
    msg=request.args.get("message")
    return render_template("templates/error.html",wrongMSG=msg)



if __name__ == '__main__':
    app.run(port=3000)

