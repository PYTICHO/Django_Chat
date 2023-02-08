let loginField = document.querySelector("#chat-login");

loginField.addEventListener("keyup", (e) => {  
    loginValue = e.target.value
    
    let data = {
        "loginValue": loginValue
    }

    
    $.ajax({ // create an AJAX call...
        data: data, // get the form data
        type: "GET", // GET or POST
        success: function(response) { // on success..
            if (loginValue.length == 0) {
                $("#loginExists").text("")
            } else if (response.loginExists) {
                $("#loginExists").text(response.loginExists)
            } else {
                $("#loginExists").text("")
                
                document.querySelectorAll(".form-error").forEach(element => {
                    element.classList.add("d-none")
                })
            }
        },
        error: function(response) { 
            
        }
    });
    return false
})