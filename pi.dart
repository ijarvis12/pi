import 'package:big_decimal/big_decimal.dart';
import 'dart:math';
import 'dart:io';

void main() {
        // start stopwatch for runtime total
        var watch = Stopwatch();
        watch.start();


        // initialize constants and vars

        int P = 1750;
        var pi = BigDecimal.parse('0').withScale(P);

        var one = BigDecimal.parse('1').withScale(P);
        var four = BigDecimal.parse('4').withScale(P);
        var two = BigDecimal.parse('2').withScale(P);

        var sixteen = BigDecimal.parse('16');
        var eight = BigDecimal.parse('8');
        var five = BigDecimal.parse('5');
        var six = BigDecimal.parse('6');

        var bigK = BigDecimal.parse('0');
        var hex = BigDecimal.parse('1').withScale(P);

        var four2 = BigDecimal.parse('1').withScale(P);
        var two2 = BigDecimal.parse('1').withScale(P);
        var one2 = BigDecimal.parse('1').withScale(P);
        var one3 = BigDecimal.parse('1').withScale(P);


        // do calculation
        for (int k = 0; k < 1447; k++) {
                bigK = BigDecimal.parse(k.toString());
                hex = one.divide(sixteen.pow(k));
                four2 = four.divide(eight*bigK+one);
                two2 = two.divide(eight*bigK+four);
                one2 = one.divide(eight*bigK+five);
                one3 = one.divide(eight*bigK+six);

                pi += (hex*(four2-two2-one2-one3)).withScale(P);
        }

        // stop stopwatch for runtime total
        watch.stop();
        var time = watch.elapsedMilliseconds / 1000;

        print(pi.withScale(P));
        print('Total calculation time: $time');
        print("Press <Enter> to end program.");
        String? _ = stdin.readLineSync()!;
}
