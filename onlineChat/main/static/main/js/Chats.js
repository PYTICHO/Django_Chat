let loginField = document.querySelector("#loginField")

loginField.addEventListener("keyup", (el) => {
    loginValue = el.target.value

    $.ajax({
        data: {'loginValue': loginValue},
        type: "GET",
        success: function(response) {
            var content = $(".chats-content", response);
            $(".chats").html(content);// update the DIV

            var error = $(".error-search-text", response);
            $(".error-search").html(error);// update the DIV
        }
    })
})