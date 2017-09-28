# HttpAuto
这是一个接口自动化框架，已经封装完成了

##实现功能
1：数据分离，Basic数据放在Excel里面
2：配置分离，配置读写通过放在.ini文件中
3：精确计算利息和服务费
4：日期计算（timedelta）

##Menu
-config
--db_config.ini    #数据库配置
--env_config.ini   #环境切换开关
--Http_config.ini  #URL配置
--server_config.ini  #服务器配置
-testdata
--ratedate.xlsx   #费率Basic数据
-operate
--datacalc   #日期计算
--rateCalcRule #费率计算
-testcase
--ts_rate_calculate #费率计算接口
---kaola_rate_14.py #考拉费率（14天）计算
---kaola_rate_30.py #考拉费率（30天）计算
--ts_rate_management #费率管理相关接口

##后续考虑
可能会封装一个界面和定时任务执行脚本
