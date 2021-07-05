$(document).ready(function (){
    setInterval(function (){
        $.ajax({
            type: "GET",
            url: "/getTime",
            success: function (response){
                console.log(response)
                document.getElementById("time").innerHTML = '';
                var c_time = response.time[0] + ' : ' + response.time[1] + ' : ' + response.time[2];
                console.log(c_time);
                document.getElementById("time").innerHTML = c_time;
            },
            error: function (response){
                console.log("An error occurred! Probably, server is not running!")
            }
        })
    }, 1000)
})