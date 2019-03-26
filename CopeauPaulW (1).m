ap=input('Profondeur de passe ?');
o=input('Longueur onde usinage ?');
r=input('Rayon outil de coupe ?');
z=input('Nombre de couteaux ?');

%Epaisseur moyenne du copeau
epmoy=(o)*((ap/(r*2))^(1/2))
%Angle effectué par le couteau pendant l'usinage d'un copeau 
ra=acos((r-ap)/r);
%Balayage du couteau de 0 à ra (définition des limites de l'équation
%paramètrique
t=-[0:0.0001:ra];
%rayon du pignon de maintien du porte outil (ici 1/2po)
rp=12.7;
%Equation de martelloti en X et Y
X=rp*(t)-r*sin(t);
Y=r*(1-cos(t));
%Graphique
plot(X,Y,'b',(X+o),Y,'b','linewidth',1.5);
axis([0 17 0 2]);
grid on;
debx=rp*-ra-r*sin(-ra);
finx=(rp*-ra-r*sin(-ra))+o;
deby=r*(1-cos(-ra));
finy=r*(1-cos(-ra));
hold on;
plot([debx finx],[deby finy],'b','linewidth',1.5);
title('Forme théorique du copeau');
xlabel('mm'); 
ylabel('mm');
text(9,1.9,{'Epaisseur moyenne du copeau=',epmoy});

