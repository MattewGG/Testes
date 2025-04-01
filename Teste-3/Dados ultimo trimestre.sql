use TesteTres;
SELECT 
    dc.data, 
    dc.cd_conta_contabil, 
    dc.vl_saldo_final 
FROM 
    demonstracoes_contabeis dc 
WHERE 
    dc.data >= '2024-10-01' AND dc.data <= '2024-12-31';