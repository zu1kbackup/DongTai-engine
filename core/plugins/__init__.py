#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: owefsad@huoxian.cn
# datetime: 2021/10/22 下午2:26
# project: DongTai-engine

from dongtai.models.project import IastProject
from dongtai.models.strategy import IastStrategyModel
from dongtai.utils import const


def is_strategy_enable(vul_type, method_pool):
    try:
        vul_strategy = IastStrategyModel.objects.filter(
            vul_type=vul_type,
            state=const.STRATEGY_ENABLE,
            user_id__in=(1, method_pool.agent.user.id)
        ).first()
        if vul_strategy is None:
            return False
        project_id = method_pool.agent.bind_project_id
        project = IastProject.objects.filter(id=project_id).first()
        if project is None:
            return False
        strategy_ids = project.scan.content
        if strategy_ids is None:
            return False
        if str(vul_strategy.id) in strategy_ids.split(','):
            return True
        return False
    except Exception as e:
        return False
