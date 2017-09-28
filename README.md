# HttpAuto接口自动化测试框架
这是一个接口自动化框架，已经封装完成了

##实现功能
1：数据分离，Basic数据放在Excel里面 </br>
2：配置分离，配置读写通过放在.ini文件中</br>
3：精确计算利息和服务费</br>
4：日期计算（timedelta）</br>

##Menu</br>
-config</br>
--db_config.ini    #数据库配置</br>
--env_config.ini   #环境切换开关</br>
--Http_config.ini  #URL配置</br>
--server_config.ini  #服务器配置</br>
-testdata</br>
--ratedate.xlsx   #费率Basic数据</br>
-operate</br>
--datacalc   #日期计算</br>
--rateCalcRule #费率计算</br>
-testcase</br>
--ts_rate_calculate #费率计算接口</br>
---kaola_rate_14.py #考拉费率（14天）计算</br>
---kaola_rate_30.py #考拉费率（30天）计算</br>
--ts_rate_management #费率管理相关接口</br>

##后续考虑</br>
可能会封装一个界面和定时任务执行脚本</br>
