from train import Train


aller = [
    Train.parse('TER', '88503', days='S', nancy='6:50', metz='7:27'), # 40€
    Train.parse('TGV', '9877', days='S', metz='7:58', besancon_tgv='10:46'),
    Train.parse('TER', '894518', days='LMaMeJVS', besancon_tgv='11:04', besancon_viotte='11:19'),

    Train.parse('TER', '835013', days='LMaMeJV', nancy='7:14', strasbourg='8:42'), # 50€
    Train.parse('TGV', '9877', days='LMaMeJV', strasbourg='9:05', besancon_tgv='10:46'),

    Train.parse('TER', '836380', days='LMaMeJV', nancy='7:54', dijon='10:29'), # 45€
    Train.parse('TER', '836380', days='S', nancy='7:58', dijon='10:29'), 
    Train.parse('TER', '894213', days='LMaMeJVS', dijon='11:09', besancon_viotte='12:05'),
    Train.parse('TGV', '6741', days='S', dijon='11:36', besancon_viotte='12:06'),

    Train.parse('TER', '835015', days='LMaMeJV', nancy='8:14', strasbourg='9:41'), # 50€
    Train.parse('TER', '835041', days='D', nancy='8:16', strasbourg='9:41'),
    Train.parse('TER', '832361', days='LMaMeJV', strasbourg='10:21', mulhouse='11:14'),
    Train.parse('TER', '96217', days='D', strasbourg='10:51', mulhouse='11:44'),
    Train.parse('TGV', '6704', days='LMaMeJV', mulhouse='11:58', besancon_tgv='12:43'),
    Train.parse('TGV', '6704', days='D', mulhouse='12:01', besancon_tgv='12:47'),
    Train.parse('TER', '894566', days='LMaMeJVD', besancon_tgv='13:39', besancon_viotte='13:54'),

    Train.parse('TER', '835755', days='LMaMeJV', nancy='8:55', epinal='9:53'), # 40€
    Train.parse('TER', '894609', days='LMaMeJV', epinal='9:59', belfort_ville='11:25'),
    Train.parse('TER', '894026', days='LMaMeJV', belfort_ville='11:36', besancon_viotte='12:46'),

    Train.parse('TER', '839161', days='LMaMeJV', nancy='11:00', strasbourg='12:33'), # 50€
    Train.parse('TER', '835043', days='D', nancy='11:16', strasbourg='12:41'),
    Train.parse('TGV', '9879', days='LMaMeJVD', strasbourg='13:03', besancon_tgv='14:44'),
    Train.parse('TER', '894528', days='LMaMeJVD', besancon_tgv='14:54', besancon_viotte='15:09'),

    Train.parse('TGV', '5537', days='LMaMeJVS', nancy='12:10', besancon_tgv='15:39'), # 30€
    Train.parse('TGV', '5537', days='D', nancy='12:27', besancon_tgv='15:39'),
    Train.parse('TER', '894575', days='LMaMeJVSD', besancon_tgv='15:48', besancon_viotte='16:01'),

    Train.parse('TER', '834024', days='LMaMeJV', nancy='12:55', epinal='13:53'), # 40-45€
    Train.parse('TER', '835819', days='S', nancy='13:20', epinal='14:18'),
    Train.parse('TGV', '2571', days='LMaMeJV', nancy='14:05', epinal='14:47'),
    Train.parse('TER', '894619', days='LMaMeJVS', epinal='14:59', belfort_ville='16:25'),
    Train.parse('TER', '894040', days='LMaMeJV', belfort_ville='16:36', besancon_viotte='17:46'),
    Train.parse('TER', '894034', days='S', belfort_ville='17:04', besancon_viotte='18:28'),

    Train.parse('TER', '835021', days='LMaMeJV', nancy='14:15', strasbourg='15:41'), # 35€
    Train.parse('TER', '835045', days='D', nancy='14:15', strasbourg='15:43'),
    Train.parse('TGV', '9580', days='LMaMeJVD', strasbourg='16:14', besancon_tgv='17:55'),
    Train.parse('TER', '894538', days='LMaMeJVD', besancon_tgv='18:07', besancon_viotte='18:22'),

    Train.parse('TER', '836382', days='LMaMeJVD', nancy='16:54', dijon='19:27'), # 45€
    Train.parse('TGV', '9896', days='LMaMeJVD', dijon='19:46', besancon_tgv='20:12'),
    Train.parse('TER', '894560', days='D', besancon_tgv='20:20', besancon_viotte='20:35'),
    Train.parse('TER', '894560', days='LMaMeJV', besancon_tgv='20:22', besancon_viotte='20:37'),
    Train.parse('TER', '894267', days='LMaMeJVD', dijon='19:50', besancon_viotte='20:55'),

    Train.parse('TER', '835771', days='S', nancy='16:20', epinal='17:18'), # 40€
    Train.parse('TER', '835775', days='LMaMeJVD', nancy='17:55', epinal='18:53'),
    Train.parse('TER', '894627', days='LMaMeJVSD', epinal='18:59', belfort_ville='20:25'),
    Train.parse('TER', '894062', days='LMaMeJVSD', belfort_ville='20:36', besancon_viotte='21:49'),
]

retour = [
    Train.parse('TER', '894208', days='LMaMeJVS', besancon_viotte='9:56', dijon='10:50'), # 45€
    Train.parse('TER', '836385', days='LMaMeJVS', dijon='11:00', nancy='13:29'),

    Train.parse('TER', '894517', days='LMaMeJV', besancon_viotte='9:55', besancon_tgv='10:10'), # 35€
    Train.parse('TER', '894517', days='S', besancon_viotte='10:12', besancon_tgv='10:27'),
    Train.parse('TGV', '9898', days='LMaMeJVS', besancon_tgv='10:34', metz='13:24'),
    Train.parse('TER', '88526', days='LMaMeJVS', metz='13:32', nancy='14:11'),

    Train.parse('TER', '894521', days='LMaMeJVSD', besancon_viotte='11:40', besancon_tgv='11:52'), # 35€
    Train.parse('TGV', '9583', days='LMaMeJVSD', besancon_tgv='12:03', strasbourg='13:43'),
    Train.parse('TER', '835020', days='LMaMeJV', strasbourg='14:18', nancy='15:44'),
    Train.parse('TER', '835034', days='S', strasbourg='15:19', nancy='16:44'),
    Train.parse('TGV', '2588', days='D', strasbourg='15:50', nancy='17:12'),
    Train.parse('TER', '839174', days='D', strasbourg='16:19', nancy='16:45'),

    Train.parse('TER', '894569', days='D', besancon_viotte='12:23', besancon_tgv='12:36'), # 50€
    Train.parse('TGV', '6705', days='D', besancon_tgv='13:31', mulhouse='14:17'),
    Train.parse('TER', '832326', days='D', mulhouse='14:34', strasbourg='15:39'),
    Train.parse('TER', '2588', days='D', strasbourg='15:50', nancy='17:12'),

    Train.parse('TER', '894563', days='LMaMeJVSD', besancon_viotte='13:38', besancon_tgv='13:55'), # 30-40€
    Train.parse('TGV', '5516', days='LMaMeJV', besancon_tgv='14:11', nancy='17:30'),
    Train.parse('TGV', '5516', days='S', besancon_tgv='14:11', nancy='17:16'),
    Train.parse('TGV', '5516', days='D', besancon_tgv='14:11', nancy='17:33'),

    Train.parse('TER', '894031', days='LMaMeJV', besancon_viotte='15:11', belfort_ville='16:24'), # 40€
    Train.parse('TER', '894624', days='LMaMeJV', belfort_ville='17:05', epinal='18:34'),
    Train.parse('TER', '834026', days='LMaMeJV', epinal='18:43', nancy='19:40'),

    Train.parse('TER', '894535', days='S', besancon_viotte='17:35', besancon_tgv='17:48'), # 40€
    Train.parse('TGV', '5500', days='S', besancon_tgv='18:23', metz='21:38'),
    Train.parse('TER', '88616', days='S', metz='22:34', nancy='23:11'),

    Train.parse('TER', '894264', days='D', besancon_viotte='18:12', dijon='19:15'), # 45€
    Train.parse('TGV', '6764', days='D', besancon_viotte='18:36', dijon='19:22'),
    Train.parse('TER', '894226', days='LMaMeJV', besancon_viotte='18:56', dijon='19:50'),
    Train.parse('TER', '836389', days='LMaMeJVD', dijon='20:05', nancy='22:31'),

    Train.parse('TER', '894559', days='SD', besancon_viotte='19:28', besancon_tgv='19:41'), # 40€
    Train.parse('TGV', '9896', days='SD', besancon_tgv='20:15', metz='22:57'),
    Train.parse('BUS', '35441', days='SD', metz='23:39', nancy='1:16'),
]
