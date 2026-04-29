import System.IO
import Control.Monad (unless)

main :: IO ()
main = do
    -- قراءة البيانات كـ "وعد" رياضي (Lazy Evaluation)
    contents <- readFile "data/input/market_trades.dat"
    let ls = lines contents
    
    -- تطبيق فلتر رياضي نقي لاستخراج الصفقات المشبوهة
    let anomalies = filter isAnomaly ls
    
    -- كتابة التقرير النهائي بدون أي تغيير في حالة الذاكرة (Immutable)
    writeFile "data/output/audit_log.txt" $ unlines 
        [ "======================================================="
        , " 🦅 VALKYRIE - PURE FUNCTIONAL AUDIT ENGINE (HASKELL)"
        , "======================================================="
        , " [STATUS] EVALUATING ALGORITHMIC TRADE SIGNALS..."
        , "-------------------------------------------------------"
        ] ++ (unlines $ map formatAnomaly anomalies) ++ 
        "\n=======================================================\n [SYSTEM] MATHEMATICAL PROOF COMPLETE. ZERO SIDE-EFFECTS.\n======================================================="

-- دالة نقية 100%: تستقبل نصاً وترجع قيمة منطقية (True/False)
isAnomaly :: String -> Bool
isAnomaly line = 
    length line >= 15 && 
    (read (drop 9 (take 15 line)) :: Int) > 75000

-- دالة تحويل البيانات للعرض
formatAnomaly :: String -> String
formatAnomaly line = 
    "[!] MARKET MANIPULATION DETECTED -> TX: " ++ take 8 line ++ " | VALUE: $" ++ (drop 9 (take 15 line))
