$(document).ready(function(){

    $("#login.html#Ingresar").click(function(){

        var username = $("login.html#Usuario").val()
        var password = $("login.html#Pass").val()
        var matchFound = false;
        var objeto_actual = null;
        var session = null;

        $.ajax({
            type: 'GET',
            url: 'https://6462ab527a9eead6fad44ee0.mockapi.io/users',
            beforeSend: function(){
              $("#login").html("Cargando...");
            },
            error: function(xhr, textStatus, error){
              console.log(xhr.statusText);
              console.log(textStatus);
              console.log(error);
            },
            success: function(data){
              $("#index").html(data)
                         

                $.each(data, function(index, obj) {
                    if (obj.username === username && obj.password === password) {
                        matchFound = true;
                        objeto_actual = obj
                    }
                });
                
                if (matchFound) {
                    console.log("¡La combinación de username y password coincide!");
                    console.log(objeto_actual.id)
                    console.log(objeto_actual.username)
                    console.log(objeto_actual.password)
                    console.log(objeto_actual.name)
                    console.log(objeto_actual.avatar)

                    $("#capa").append("<p>Username: "+objeto_actual.username+"</p>")
                    $("#capa").append("<img src='"+objeto_actual.avatar+"' />")

                    session = objeto_actual.username
                    localStorage.setItem("x", session);




                } else {
                    console.log("La combinación de username y password no coincide.");
                }
                

            }
        });
        
    });
    

    $("#btnRegistrar").click(function(){
        
        var us = $("#txtUser").val()
        var pass = $("#txtPass").val()
        var na = $("#txtName").val()
        var ava = $("#txtAvatar").val()

        var objeto = {
            username: us,
            password: pass,
            name: na,
            avatar: ava
        }

        $.ajax({
            type: 'POST',
            data: objeto,
            url: 'https://6462ab527a9eead6fad44ee0.mockapi.io/users',
            beforeSend: function(){
                $("#capa").html("<img src='assets/img/cargando.gif' />")
            },
            error: function(xhr, status, error){
                console.log(error)
            },
            success: function(data){
                $("#capa").html("<h1>Registrado OK:</h1>")
                $("#capa").append(data)
            }
        })

    });


});