from os import remove

from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Obstacle import Obstacle
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Obstacle):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, Player):
            if ent.rect.bottom > WINDOW_HEIGHT:
                ent.health = 0
        pass

    @staticmethod
    def __verify_collision_entity(ent1: Entity, ent2: Entity):
        valid_instance = False
        if isinstance(ent1, Player) and isinstance(ent2, Obstacle):
            valid_instance = True
        elif isinstance(ent1, Obstacle) and isinstance(ent2, Player):
            valid_instance = True

        if valid_instance:
            if ent1.rect.right >= ent2.rect.left and ent1.rect.left <= ent2.rect.right and ent1.rect.bottom >= ent2.rect.top and ent1.rect.top <= ent2.rect.bottom:
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage

    @staticmethod
    def __give_score(player: Player, entity_list: list[Entity]):
        for ent in entity_list:
            if isinstance(ent, Obstacle):
                if player.rect.centerx > ent.rect.centerx:
                    player.score += ent.score
        pass

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for entity1 in entity_list:
            EntityMediator.__verify_collision_window(entity1)

            for entity2 in entity_list[+1:]:
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)

