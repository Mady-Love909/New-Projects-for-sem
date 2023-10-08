let forgotpassword = document.getElementById("forgotpassword")
        let password = document.getElementById("password")
        let passwordtxt = document.getElementById("passwordtxt")
        let modalbtn = document.getElementById('modalbtn')
        let modalformbtn = document.getElementById('modalformbtn')
        document.getElementById('modal').style.display = "none"

        let btn1 = document.getElementById('btn1')

        btn1.addEventListener('click', () => {
            document.getElementById('modal').style.display = "block"

        })
        btn2.addEventListener('click', () => {
            document.getElementById('modal').style.display = "block"

        })
        modalbtn.addEventListener('click', () => {
            document.getElementById('modal').style.display = "none"
        })
        let signupbtn = document.getElementById('signupbtn')
        let signupchange = () => {
            let fullname = document.createElement('input')
            fullname.inputMode = Number

            document.getElementById('loginform').appendChild(fullname)
            forgotpassword.style.display = "none"
            password.style.display = "none"
            passwordtxt.style.display = "none"
            modalformbtn.innerHTML = "Register"

        }
        signupbtn.addEventListener('click', signupchange)
        if (modalformbtn.innerHTML == "Register") {
            signupbtn.removeEventListener('click', signupchange)
        }