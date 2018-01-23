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
# 生成模板
shopids=`cat shopids.txt`
dataj=`cat datax.json`
dataj=${dataj//reader-host/${HOST}}
dataj=${dataj//reader-port/${PORT}}
dataj=${dataj//reader-database/${DATABASE}}
dataj=${dataj//reader-username/${USERNAME}}
dataj=${dataj//reader-password/${PASSWORD}}
dataj=${dataj//writer-host/${WHOST}}
dataj=${dataj//writer-port/${WPORT}}
dataj=${dataj//writer-database/${WDATABASE}}
dataj=${dataj//writer-username/${WUSERNAME}}
dataj=${dataj//writer-password/${WPASSWORD}}
dataj=${dataj//shop-id-place/${shopids}}
# 查看文件夹是否存在
if [ ! -d "./job" ]; then
  mkdir ./job
fi
# 获取所有表名，替换
# mysql -h jixiao.test.superboss.cc -P 3306 -udev -pguanghua -e "use jixiao_fanjinlong;show tables;" > catfilename
tables=`echo "select table_name from information_schema.tables where table_schema = '${DATABASE}' and table_type = 'BASE TABLE';" | mysql -h ${HOST} -P ${PORT} -u${USERNAME} -p${PASSWORD}`
for i in $tables;
do
    job=${dataj//table-place/${i}}
    echo ${job} > job/${i}.json
done