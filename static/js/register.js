// alert("注册项准备完成！")
function bindEmailCaptchaClick(){
    $("#captcha-btn").click(function (event) {
    // $this: 代表当前按钮的jQuery对象
    var $this = $(this);
    // 阻止默认事件
    event.preventDefault();

        var email = $("input[name='email']").val();
        // alert(email);
        $.ajax({
            // http://192.168.3.101:5000
            url: "/space/captcha/email?email="+email,
            method: "GET",
            success: function (result) {
                console.log(result);
                var code = result['code'];
                if(code == 200){
                    var countdown = 5;
                    // 开始倒计时，取消按钮点击事件
                    $this.off("click");
                    var timer = setInterval(function () {
                        $this.text(countdown);
                        countdown -= 1;
                        // 倒计时结束
                        if(countdown <= 0){
                            // 清理计算器
                            clearInterval(timer);
                            // 重置按钮文字
                            $this.text("获取验证码");
                            // 重新绑定点击事件
                            bindEmailCaptchaClick();
                        }
                    }, 1000);
                    alert("邮箱验证码已发送！");
                }else{
                    alert(result['msg']);
                }
            },
            fail: function (error) {
                console.log(error);
            }
        })
    });
}

$(function (){
    bindEmailCaptchaClick()
});