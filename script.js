function checkCaptcha() {
    const captcha = document.getElementById("captcha").textContent;
    const userInput = document.getElementById("input-captcha").value;
    const result = document.getElementById("result");

    if(userInput === captcha){
        result.textContent = "Captcha solved!";
    } else {
        result.textContent = "Incorrect. Try again.";
    }
}
