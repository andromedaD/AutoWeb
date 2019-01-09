# AutoWeb
这是一个web ui自动化框架，框架为分层结构：   PS：以下不写上层路径的表示本层目录  <Br/>
action:   <Br/>
      - Pageaction: web页面操作封装，如click、find_element、swicth_new_window、open_broswer、forward、backup等，可自行添加   <Br/>
      - choose_data: 用于多浏览器自动切换，runtest/runtest.py存在一个写入方法，讲当前浏览器driver结果输入此文件，driver.py将    
                    choose_data作为broswer()方法的传入参数，生成对应的driver以供testscripts里的脚本调用   <Br/>
      - driver.py: 生成driver供调用

conf:    <Br/>
    - config.py: 将config.yaml文件参数化   <Br/>
    - config.yaml: 全局配置文件，如smtp配置等    <Br/>
    
runtest:  <Br/>
				-runtest.bak.py 早期版本的执行文件   <Br/>
				-runtest.py   相对早期版本多了一个自动切换driver   <Br/>
			
test_data:  用于testscrpts各个脚本，里面参数有定位元素和输入的文本信息  <Br/>

test_report:   <Br/>
					- logs: 用于存放脚本执行中的log  <Br/>
					- image: 用于存放网页截图，实际脚本没有用Pageaction的截图方法  <Br/>
					- *result.html: 测试报告  <Br/>
			
testscripts: 用于各个模块实际的脚本文件   <Br/>

util: <Br/>
		- baidumap_requests.py: 成输入小区名字的经纬度，接口url为url='http://api.map.baidu.com/geocoder'     <Br/>
		- hash_value.py: 输入参数返回hashvalue参数  <Br/>
		- image_recongirition.py: 别图片验证码，暂未实现   <Br/>
	  - keyboardUtil.py: 期代码，键盘方法，已屏蔽   <Br/>
		- log_print.py: 志输出工具包，配置写死的   <Br/>
		- myutil.py: 为使用最频繁的工具包，作为unittest的setUp和tearDown方法封装   <Br/>
		- send_email.py: 动发送邮件   <Br/>
		
	
