$(document).ready(function(){
  console.log("loaded");


  $(document).on("submit", "#register-form", function(e){
    e.preventDefault();
    console.log("Form submitted");
    //var form =  $("#register-form").serialize();

    data1 =
    {username : $("#username").val(), password: $("#password").val()};
    console.log(data1);
    $.ajax({
      url: "/postregister",
      type: "POST",
      data: data1,
      success: function(response){
        console.log(response);

      }

    });
  });

  $(document).on("submit", "#login-form", function(e){
    e.preventDefault();
    console.log("Login js func");
    data1 = {username: $("#username_lgn").val(), password: $("#password_lgn").val()}
    console.log(data1);
    $.ajax({
      url: "/postlogin",
      type: "POST",
      data: data1,
      success : function(response){
        console.log(response);
        if(response == "OK"){
          window.location.href="/"
        }
      }
    });
  });


  $(document).on("click", "#login_link", function(e){
    e.preventDefault();

  });
});
