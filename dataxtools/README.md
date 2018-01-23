# 使用手册
 1. 在reader.txt配置需要迁移的数据库
 2. writer.txt配置需要目标库
 3. shopids中配置需要迁移的店铺id，用英文逗号分隔
 4. 执行sh data_tool.sh，生成的文件在job目录
 5. 批量执行datax任务 find job -name "*.json" -exec python datax.py {} \; && echo "全部执行结束"
 6. 执行sh data_check.sh 查询下有没有数据不一致的表