#!/bin/sh

YOUR_GSLT=D97FEDAD30E61BFA902FA2259C66371B
CSGO_INSTALL_LOCATION="/root/Steam/csgo-ds/"

cd $CSGO_INSTALL_LOCATION
screen -S "Counter-Strike: Global Offensive Server" ./srcds_run -game csgo -usercon +game_type 0 +game_mode 1 +mapgroup mg_bomb +map de_dust2 +sv_setsteamaccount $YOUR_GSLT -net_port_try 1