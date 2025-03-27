!function() {
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    asrsea = d,
    ecnonasr = e
}();
var ZA7t = undefined;
if (e4i.useNewEncrypt) {
    if (e4i.headers && typeof e4i.headers === "object") {
        e4i.headers[mT7M.ehk] = mT7M.ehv
    } else {
        e4i.headers = {};
        e4i.headers[mT7M.ehk] = mT7M.ehv
        }
        ZA7t = asrsea(JSON.stringify(i4m), Ob5g(["怒", "流感"], mT7M.nemj), Ob5g(mT7M.nmd, mT7M.nemj), Ob5g(["可爱", "钻石", "跳舞", "生病"], mT7M.nemj))
    } else {
        ZA7t = asrsea(JSON.stringify(i4m), Ob5g(["流泪", "强"], mT7M.emj), Ob5g(mT7M.md, mT7M.emj), Ob5g(["爱心", "女孩", "惊恐", "大笑"], mT7M.emj))
        }
            // e4i.data = j4n.cq4u({
            //     params: ZA7t.encText,
            //     encSecKey: ZA7t.encSecKey
            // })

console.log(ZA7t)