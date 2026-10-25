##Neden dekoratörlerin yeri değiştiğinde sonuçlar değişiyor?

####dekoratörler ile çalışan fonksiyonlar tabiri caizse soğan gibi katmanlı bir yapı ile çalışır.

örnek;

fib3  = lru_cache(say(fib3))
-lru_cache önce bu değer daha önce hesaplandı mı diye kontrol eder, hesaplandı ise direk sonucu döndürür. eğer hesaplanmadıysa;
-say fonksiyonu bu işlem için .cagri değerini 1 arttırır ve bu komutun 1 kere kullanıldığını sayar
-ve nihayet soğan katmanları olarak tabir ettiğim yapının en merkezine ulaşılır ve fibonacci fonksiyonunu kendisi çalışır.

aynı bir soğanın katmanları dıştan içe doğru bir yol izlenir.

bu sebeple 

fib1() fonksiyonu çalışırken sadece her fonkisyon çalıştığında @say dekoratörü sayım yapar. ancak fib1(20)'i hesaplamak için her fib20 için fib 19 fib ve fib 18, fib 19 için fib18 ve fib17, fib18 için fib17 ve fib16... teker teker hesaplanır. bu sebeple fib1(20) 21891 sonucunu döndürür. devasa bir işlem yükü.

fib2() fonksiyonu çalışırken [say(lru_cache(fib2))] say dekoratörü başta olduğu için ilk önce bütün işlemler sayılır. sayıldıktan sonra lru_cache bu değerin (örneğin fib18) hesaplanıp hesaplanmadığına bakar ve ya değeri döndürür ya da değeri hesaplamamışsa değeri hesaplar. Bu sebeple fib2(20) 39 değerini hesaplar.

fib3() fonksiyonu çalışırken [lru_cache(say(fib3))] lru_cache dekoratörü başta olduğu için ilk iş olarak her zaman hesaplanacak fib değerinin daha önce hesaplanıp hesaplanmadığı kontrol edilir. hesaplandıysa direk sonuç döndürülür ve işlem hiç sayıma gitmez. Eğer bu değer hesaplanmadıysa bir alt katmana geçer ve @say dekoratörü çalışır. Bu sefer yapılan hesaplama .cagri ile sayılır. ve sayıldıktqan sonra hesaplama adımları devam ede. bu fonksiyonda lru_cache @say dekoratörüden öne yzoıldığıiçin daha önce hesaplanan değerler sayılmamış ve çıktı olarak 21 değerini vermiştir.