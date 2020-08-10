import kotlin.random.Random

class Solution(){

    fun addition(x:Int, y:Int): Int{
        val sumNematodes =  x + y
        return wait(sumNematodes)
    }

    fun wait(nematodesNum: Int): Int{
        val left = nematodesNum % 2
        val pairs = nematodesNum / 2
        var out = 0
        for (i in 0 until pairs){
            if (Random.nextBoolean()){
                out++
            }
        }
        return out + pairs*2 + left
    }

    fun exponential(nematodesNum: Int, days:Int):Int{

        var out = wait(nematodesNum)
        when (days) {
            0 -> return nematodesNum;
            1 -> return out;
            else ->  for (i in 2..days) {
                out = wait(out)
            }
        }
        return out
    }
}
fun simulate(x: Int = 0, y: Int = 0, exp:Int = 0, numberOfSimulations:Int): Float {
    val s = Solution()
    var res:Float = 0.0F
    for (i in 1..numberOfSimulations){
        res += s.exponential(s.addition(x,y), exp)
    }
    return res/numberOfSimulations
}

fun main(){
    val s = Solution()
    print(simulate(1,1,4,10000))
}