from os import remove

from code.Const import WINDOW_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, (Enemy, EnemyShot)):
            if ent.rect.right < 0:
                ent.health = 0

        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WINDOW_WIDTH:
                ent.health = 0

        pass

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            teste_entity = entity_list[i]
            EntityMediator.__verify_collision_window(teste_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)