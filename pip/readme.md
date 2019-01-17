pip升级到10.0.1之后可能会出现这个错误
module 'pip' has no attribute 'main'
解决方法：
方法一
    网上有类似的错误描述：stackoverflow这里 
    里边提到降级处理
    python3 -m pip install --user --upgrade pip==9.0.3

方法二
    更新pip
    $curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    $python get-pip.py 或
    $python3 get-pip.py
    如果遇到consider using the '--user' option or check the permissions
    则 python3 get-pip.py --user

方法三
    重装python3
    brew reinstall python3