function solution(pt, at, logs) {
    logs = logs.map(l => l.split('-'))
    logs = [[pt,at], ...logs]
    
    logs = logs.map(log => {
        return log.map(l => {
            let [h, m, s] = l.split(':')
            return Number(h) * 3600 + Number(m) * 60 + Number(s)
        })
    })
    pt = logs[0][0]
    at = logs[0][1]
    logs = logs.splice(1)
    
    let tt = [...Array(pt+1).keys()].map(_ => 0)
    for (let i = 0; i < logs.length; i++){
        let [s,e] = logs[i]
        tt[s] += 1
        tt[e] -= 1
        }
    
    for (let i = 1; i <= pt; i++){
        tt[i] += tt[i-1]
    }
    
    for (let i = 1; i <= pt; i++){
        tt[i] += tt[i-1]
    }
    
    let result = [tt[at], 0]
    for (let i = at+1; i <= pt; i++){
        if (result[0] < tt[i]-tt[i-at]){
            result = [tt[i]-tt[i-at], i-at+1]
        }
    }
    
    result = result[1]
    let h = String(Math.floor(result/3600))
    result = result % 3600
    let m = String(Math.floor(result / 60))
    let s = String(result % 60)
    
    return [h, m, s].map(t => t.length === 2 ? t : `0${t}`).join(':')
}
solution(	"02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"])