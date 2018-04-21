clc;
close all;
clear all;

quanser_aero_lqr;
disp(K);

% Ac = [(A+B*K)];
% Bc = [B];
% Cc = [C];
% Dc = [D];
% 
% sys = ss(Ac,Bc,Cc,Dc);
% 
% % t = 0:0.01:5;
% % r =0.2*ones(size(t));
% % [y,t,x]=lsim(sys_cl,r,t);
% % [AX,H1,H2] = plotyy(t,y(:,1),t,y(:,2),'plot');
% 
% lsimplot(sys_cl);

sys = ss(A-B*K,[0;0;0;0],K,0);
t = 0:0.1:10;
u = zeros(1,length(t));
% lsim(sys,u,0:0.1:10)
initial(sys,[0;0;0.1;0],5)