
//http://d.hatena.ne.jp/chick307/20110519/1305828061

function sleepSort(array, callback, f){
    var l = array.length, result = [];
    var i = l;

    if(f == null)
        f = Number;

    while(i--) (function(value){
            setTimeout(function(){
                result.push(value);
                if(--l === 0)
                callback(result);
                }, f(value));
            })(array[i]);
}

