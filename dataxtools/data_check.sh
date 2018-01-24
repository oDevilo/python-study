#!/bin/bash
# 读取源数据库配置
READER=`cat reader.txt`
for i in $READER;
do
    tag=${i%%=*}
    case $tag in
    host)
        HOST=${i#*=}
        ;;
    port)
        PORT=${i#*=}
        ;;
    database)
        DATABASE=${i#*=}
        ;;
    username)
        USERNAME=${i#*=}
        ;;
    password)
        PASSWORD=${i#*=}
        ;;
    esac
done
# 读取目标数据库配置
WRITER=`cat writer.txt`
for i in $WRITER;
do
    tag=${i%%=*}
    case $tag in
    host)
        WHOST=${i#*=}
        ;;
    port)
        WPORT=${i#*=}
        ;;
    database)
        WDATABASE=${i#*=}
        ;;
    username)
        WUSERNAME=${i#*=}
        ;;
    password)
        WPASSWORD=${i#*=}
        ;;
    esac
done
# 获取所有表名
shopids=`cat shopids.txt`
tables=`echo "select table_name from information_schema.tables where table_schema = '${DATABASE}' and table_type = 'BASE TABLE';" | mysql -h ${HOST} -P ${PORT} -u${USERNAME} -p${PASSWORD} -N`
rm check.txt
touch check.txt
num=0
str=""
for i in $tables;
do
    if [ $i == "ts" ]; then
        echo "跳过表ts"
    else
        readerCount=`echo "use ${DATABASE};select count(*) as ct from ${i} where shop_id in (${shopids})" | mysql -h ${HOST} -P ${PORT} -u${USERNAME} -p${PASSWORD} -N`
        writerCount=`echo "use ${WDATABASE};select count(*) as ct from ${i} where shop_id in (${shopids})" | mysql -h ${WHOST} -P ${WPORT} -u${WUSERNAME} -p${WPASSWORD} -N`
        echo "开始检查--${i}--读表总数${readerCount},写表总数${writerCount}" >> check.txt
        if [ $readerCount != $writerCount ]; then
            let "num+=1"
            str=$str","${i}
        fi
    fi
done
echo "不相同表数${num},表名:${str}" >> check.txt
echo "检查结束"