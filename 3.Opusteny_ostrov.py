print('''       ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     -ART BY ZEUS-
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--`
''')
print("Vitaj na oputstenom ostrove.")
print("Tvojou ulohou je prezit a mozno najdes aj poklad kek.")
krizovatka1 = input("Dorazil si na opusteny ostrov. V pravo je husta dzungla a v lavo vysoke hory. Ktorou cestou sa vyberies? Napis \"pravo\" alebo \"lavo\"\n.")
krizovatka1 = krizovatka1.lower()
if krizovatka1 == "pravo":
  krizovatka2 = input("Hrdinsky si sa prebojoval tmavou dzunglou a prisiel si k vchodu do jaskyne. Chces vstupit? Napis \"ano\" alebo \"nie\"\n.")       
  krizovatka2 = krizovatka2.lower()
  if krizovatka2 == "ano":
    krizovatka3 = input("V jaskyni na teba caka nahnevany jaskynny troll, musis bojovat! Aku zbran si vyberies? Ak sa dnes citis a myslis, ze ho skolis holymi rukami, napis \"ruky\", alebo si zober kamen zo zeme a napis \"kamen\"\n.")
    krizovatka3 = krizovatka3.lower()
    if krizovatka3 == "ruky":
      print("Trolla si si dal ako predjedlo pred trapezovym dnom vo fitku. Gratulujem drvic ! V truhlici ktoru strazi si nasiel pol kila susenej srvatky a uteracik do sprchy. Zoberies to a makas do fitka na druje strane ostrova.")
    else:
      print("Troll sa zamsial na tvojej chabej zbrani a dal si ta ako predjedlo pred obedom. GG")
      
  else:
    print("Pri tvojom putovani dzunglou ta ustipol had. GG")   
else:
  print("V horach ta chytil Yeti, potom ta upiekol a zozral, GG.")
input('Press ENTER to exit')
  
  
      