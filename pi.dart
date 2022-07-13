import 'package:big_dart/big_dart.dart';
import 'dart:math';
import 'dart:io';

void main() {
        // start stopwatch for runtime total
        var watch = Stopwatch();
        watch.start();


        // initialize constants and vars

        int P = 1750;
        var pi = Big(0).prec(P);

        var one = Big(1);
        var four = Big(4);
        var two = Big(2);

        var sixteen = Big(16);
        var eight = Big(8);
        var five = Big(5);
        var six = Big(6);

        var bigK = Big(0);
        var hex = Big(1);

        var four2 = Big(1);
        var two2 = Big(1);
        var one2 = Big(1);
        var one3 = Big(1);


        // do calculation
        for (int k = 0; k < 1447; k++) {
                bigK = Big(k);
                hex = (one/sixteen.pow(k).prec(P)).prec(P);
                four2 = (four/(eight*bigK+one).prec(P)).prec(P);
                two2 = (two/(eight*bigK+four).prec(P)).prec(P);
                one2 = (one/(eight*bigK+five).prec(P)).prec(P);
                one3 = (one/(eight*bigK+6).prec(P)).prec(P);

                pi += (hex*(four2-two2-one2-one3)).prec(P);
        }

        // stop stopwatch for runtime total
        watch.stop();
        var time = watch.elapsedMilliseconds / 1000;

        print(pi.prec(P));
        print('Total calculation time: $time');
        print("Press <Enter> to end program.");
        String? _ = stdin.readLineSync()!;
}
