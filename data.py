from train import Train


aller = [
    Train.parse('TER', '88503', days='S', nancy='6h50', metz='7h27'), # 40€
    Train.parse('TGV', '9877', days='S', metz='7h58', besancon_tgv='10h46'),
    Train.parse('TER', '894518', days='LMaMeJVS', besancon_tgv='11h04', besancon_viotte='11h19'),

    Train.parse('TER', '835013', days='LMaMeJV', nancy='7h14', strasbourg='8h42'), # 50€
    Train.parse('TGV', '9877', days='LMaMeJV', strasbourg='9h05', besancon_tgv='10h46'),

    Train.parse('TER', '836380', days='LMaMeJV', nancy='7h54', dijon='10h29'), # 45€
    Train.parse('TER', '836380', days='S', nancy='7h58', dijon='10h29'), 
    Train.parse('TER', '894213', days='LMaMeJVS', dijon='11h09', besancon_viotte='12h05'),
    Train.parse('TGV', '6741', days='S', dijon='11h36', besancon_viotte='12h06'),

    Train.parse('TER', '835015', days='LMaMeJV', nancy='8h14', strasbourg='9h41'), # 50€
    Train.parse('TER', '835041', days='D', nancy='8h16', strasbourg='9h41'),
    Train.parse('TER', '832361', days='LMaMeJV', strasbourg='10h21', mulhouse='11h14'),
    Train.parse('TER', '96217', days='D', strasbourg='10h51', mulhouse='11h44'),
    Train.parse('TGV', '6704', days='LMaMeJV', mulhouse='11h58', besancon_tgv='12h43'),
    Train.parse('TGV', '6704', days='D', mulhouse='12h01', besancon_tgv='12h47'),
    Train.parse('TER', '894566', days='LMaMeJVD', besancon_tgv='13h39', besancon_viotte='13h54'),

    Train.parse('TER', '835755', days='LMaMeJV', nancy='8h55', epinal='9h53'), # 40€
    Train.parse('TER', '894609', days='LMaMeJV', epinal='9h59', belfort_ville='11h25'),
    Train.parse('TER', '894026', days='LMaMeJV', belfort_ville='11h36', besancon_viotte='12h46'),

    Train.parse('TER', '839161', days='LMaMeJV', nancy='11h00', strasbourg='12h33'), # 50€
    Train.parse('TER', '835043', days='D', nancy='11h16', strasbourg='12h41'),
    Train.parse('TGV', '9879', days='LMaMeJVD', strasbourg='13h03', besancon_tgv='14h44'),
    Train.parse('TER', '894528', days='LMaMeJVD', besancon_tgv='14h54', besancon_viotte='15h09'),

    Train.parse('TGV', '5537', days='LMaMeJVS', nancy='12h10', besancon_tgv='15h39'), # 30€
    Train.parse('TGV', '5537', days='D', nancy='12h27', besancon_tgv='15h39'),
    Train.parse('TER', '894575', days='LMaMeJVSD', besancon_tgv='15h48', besancon_viotte='16h01'),

    Train.parse('TER', '834024', days='LMaMeJV', nancy='12h55', epinal='13h53'), # 40-45€
    Train.parse('TER', '835819', days='S', nancy='13h20', epinal='14h18'),
    Train.parse('TGV', '2571', days='LMaMeJV', nancy='14h05', epinal='14h47'),
    Train.parse('TER', '894619', days='LMaMeJVS', epinal='14h59', belfort_ville='16h25'),
    Train.parse('TER', '894040', days='LMaMeJV', belfort_ville='16h36', besancon_viotte='17h46'),
    Train.parse('TER', '894034', days='S', belfort_ville='17h04', besancon_viotte='18h28'),

    Train.parse('TER', '835021', days='LMaMeJV', nancy='14h15', strasbourg='15h41'), # 35€
    Train.parse('TER', '835045', days='D', nancy='14h15', strasbourg='15h43'),
    Train.parse('TGV', '9580', days='LMaMeJVD', strasbourg='16h14', besancon_tgv='17h55'),
    Train.parse('TER', '894538', days='LMaMeJVD', besancon_tgv='18h07', besancon_viotte='18h22'),

    Train.parse('TER', '835771', days='S', nancy='16h20', epinal='17h18'), # 40€
    Train.parse('TER', '894627', days='S', epinal='18h59', belfort_ville='20h25'),
    Train.parse('TER', '894062', days='S', belfort_ville='20h36', besancon_viotte='21h49'),

    Train.parse('TER', '836382', days='LMaMeJVD', nancy='16h54', dijon='19h27'), # 45€
    Train.parse('TGV', '9896', days='LMaMeJVD', dijon='19h46', besancon_tgv='20h12'),
    Train.parse('TER', '894560', days='D', besancon_tgv='20h20', besancon_viotte='20h35'),
    Train.parse('TER', '894560', days='LMaMeJV', besancon_tgv='20h22', besancon_viotte='20h37'),
    Train.parse('TER', '894267', days='LMaMeJVD', dijon='19h50', besancon_viotte='20h55'),

    Train.parse('TER', '835775', days='LMaMeJVD', nancy='17h55', epinal='18h53'), # 40€
    Train.parse('TER', '894627', days='LMaMeJVD', epinal='18h59', belfort_ville='20h25'),
    Train.parse('TER', '894062', days='LMaMeJVD', belfort_ville='20h36', besancon_viotte='21h49'),
]

retour = [
    Train.parse('TER', '894208', days='LMaMeJVS', besancon_viotte='9h56', dijon='10h50'), # 45€
    Train.parse('TER', '836385', days='LMaMeJVS', dijon='11h00', nancy='13h29'),

    Train.parse('TER', '894517', days='LMaMeJV', besancon_viotte='9h55', besancon_tgv='10h10'), # 35€
    Train.parse('TER', '894517', days='S', besancon_viotte='10h12', besancon_tgv='10h27'),
    Train.parse('TGV', '9898', days='LMaMeJVS', besancon_tgv='10h34', metz='13h24'),
    Train.parse('TER', '88526', days='LMaMeJVS', metz='13h32', nancy='14h11'),

    Train.parse('TER', '894521', days='LMaMeJVSD', besancon_viotte='11h40', besancon_tgv='11h52'), # 35€
    Train.parse('TGV', '9583', days='LMaMeJVSD', besancon_tgv='12h03', strasbourg='13h43'),
    Train.parse('TER', '835020', days='LMaMeJV', strasbourg='14h18', nancy='15h44'),
    Train.parse('TER', '835034', days='S', strasbourg='15h19', nancy='16h44'),
    Train.parse('TGV', '2588', days='D', strasbourg='15h50', nancy='17h12'),
    Train.parse('TER', '839174', days='D', strasbourg='16h19', nancy='16h45'),

    Train.parse('TER', '894569', days='D', besancon_viotte='12h23', besancon_tgv='12h36'), # 50€
    Train.parse('TGV', '6705', days='D', besancon_tgv='13h31', mulhouse='14h17'),
    Train.parse('TER', '832326', days='D', mulhouse='14h34', strasbourg='15h39'),
    Train.parse('TER', '2588', days='D', strasbourg='15h50', nancy='17h12'),

    Train.parse('TER', '894563', days='LMaMeJVSD', besancon_viotte='13h38', besancon_tgv='13h55'), # 30-40€
    Train.parse('TGV', '5516', days='LMaMeJV', besancon_tgv='14h11', nancy='17h30'),
    Train.parse('TGV', '5516', days='S', besancon_tgv='14h11', nancy='17h16'),
    Train.parse('TGV', '5516', days='D', besancon_tgv='14h11', nancy='17h33'),

    Train.parse('TER', '894031', days='LMaMeJV', besancon_viotte='15h11', belfort_ville='16h24'), # 40€
    Train.parse('TER', '894624', days='LMaMeJV', belfort_ville='17h05', epinal='18h34'),
    Train.parse('TER', '834026', days='LMaMeJV', epinal='18h43', nancy='19h40'),

    Train.parse('TER', '894535', days='S', besancon_viotte='17h35', besancon_tgv='17h48'), # 40€
    Train.parse('TGV', '5500', days='S', besancon_tgv='18h23', metz='21h38'),
    Train.parse('TER', '88616', days='S', metz='22h34', nancy='23h11'),

    Train.parse('TER', '894264', days='D', besancon_viotte='18h12', dijon='19h15'), # 45€
    Train.parse('TGV', '6764', days='D', besancon_viotte='18h36', dijon='19h22'),
    Train.parse('TER', '894226', days='LMaMeJV', besancon_viotte='18h56', dijon='19h50'),
    Train.parse('TER', '836389', days='LMaMeJVD', dijon='20h05', nancy='22h31'),

    Train.parse('TER', '894559', days='SD', besancon_viotte='19h28', besancon_tgv='19h41'), # 40€
    Train.parse('TGV', '9896', days='SD', besancon_tgv='20h15', metz='22h57'),
    Train.parse('BUS', '35441', days='SD', metz='23h39', nancy='1h16'), # be careful with time in past
]