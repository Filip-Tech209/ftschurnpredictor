<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>FTS_Churn Predictor Login</title>
</head>
<body>

<!-- ------------------php code start here------------------ -->
    <?php
        if(isset($_POST['register'])){
            echo "details submitted"
        }
    ?>
<!-- ------------------php code ends here------------------ -->
    <div class="wrapper">
        <section class="form signup">
            <header>Login </header>
            <form  action="#" method="POST">
                <div class="error-txt">This is error message!</div>
                <!-- <div class="name-details"> -->
                    <div class="field input">
                        <label for="">Email Address</label>
                        <input name="Email" type="email">
                    </div>
                <!-- </div> -->
                    <div class="field input">
                        <label for="">Password</label>
                        <input name="pass1" type="password">
                    </div>
                    <div class="field button">
                        <input name="register" type="submit"value="Login Now">
                    </div>
             </form>
            <div class="link">Don`t Have an account?<a href="user_Register.html">Register</a></div>
        </section>
    </div>

  <style>
      *{
          margin: 0px;
          padding: 0px;
          box-sizing: border-box;
          text-decoration: none;
          font-family: 'Poppins',sans-serif;
      }
      body{
          display: flex;
          align-items: center;
          justify-content: center;
          min-height: 100vh;
          background: #f7f7f7;
      }
    .wrapper{
        background: #fff;
        width: 450px;
        height: auto;
        border-radius: 16px;
        box-shadow: 0 0 128px 0 rgba(0,0,0,0.1),
                    0 32px 64px -48px rgba(0,0,0,0.5);
    }
    /* Signup form CSS Code */
    .form{
        padding: 25px 30px;
    }
    .form header{
        font-size: 25px;
        font-weight: 600;
        padding-bottom: 10px;
        border-bottom: 1px solid #e6e6e6;
    }
    .form form{
        margin: 20px 0;
    }
    .form form .error-txt{
        color: #721c24;
        background: #f8d7da;
        padding: 8px 10px;
        text-align: center;
        border-radius: 5px;
        margin-bottom: 10px;
        border-radius: 1px #f5c6cb;
    }
    .form form .name-details{
        display: flex;
    }
    form .name-details .field:first-child{
        margin-right: 10px;
    }
    form .name-details .field:last-child{
        margin-left: 10px;
    }
    form .name-details .field label{
        margin-right: 2px;
    }
    .form form .field{
        display: flex;
        flex-direction: column;
        margin-bottom: 10px;
    }
    .form form .field input{
        outline: none;
    }
    .form form .field label{
        font-weight: 600;
        color: #000000;
    }
    .form form .input input{
        height: 40px;
        width: 100%;
        font-size: 16px;
        border-radius: 4px;
        padding: 10px 10px;
        border: 1px solid #ccc;
    }
    .form form .image input{
       font-size: 17px;
    }
    .form form .button input{
        margin-top: 13px;
        height:45px ;
        border: none;
        font-size: 17px;
        font-weight: 400;
        background: rgb(13, 64, 160);
        color:#fff;
        border-radius: 5px;
        cursor: pointer;
    }
    .form form .button input:hover{
        background: rgb(2, 143, 49);
    }
    .form .link{
        text-align: center;
        margin: 10px 0;
        font-size: 17px;
    }
    .form .link a{
        color: #333;
    }
    .form .link a:hover{
        text-decoration: underline;
        color: rgb(13, 64, 160);
    }
  </style>  
</body>
</html> 