$(document).ready(function() {
    let currentUrl = location.pathname
    if (currentUrl == "/profile/")
        setTimeout(function(){
        $("#eddit-profile").modal('show');
    }, 1000)
});

// alert(location.pathname);