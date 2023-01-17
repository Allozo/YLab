from sqlalchemy.orm import Session

from menu import models, schemas


def get_all_menu(db: Session) -> list[schemas.MenuBase]:
    res = db.query(models.Menu).all()
    return res


def get_menu_by_id(menu_id: str, db: Session) -> schemas.Menu:
    return db.query(models.Menu).filter(models.Menu.id == menu_id).first()


def create_menu(menu: schemas.MenuBase, db: Session) -> schemas.Menu:
    menu_db = models.Menu(
        title=menu.title,
        description=menu.description,
        submenus_count=0,
        dishes_count=0,
    )
    db.add(menu_db)
    db.commit()
    db.refresh(menu_db)
    return menu_db


def delete_menu(menu_id: str, db: Session) -> None:
    menu_db = get_menu_by_id(menu_id, db)
    db.delete(menu_db)
    db.commit()


def update_menu(
    old_menu: schemas.Menu, new_menu: schemas.MenuBase, db: Session
) -> schemas.MenuBase:
    old_menu.title, old_menu.description = new_menu.title, new_menu.description
    db.add(old_menu)
    db.commit()
    db.refresh(old_menu)
    return old_menu


def get_all_submenu(menu_id: str, db: Session):
    res = db.query(models.Submenu).filter(models.Menu.id == menu_id).all()
    return res


def get_submenu_by_id(menu_id: str, submenu_id: str, db: Session):
    res = (
        db.query(models.Submenu)
        .filter(models.Menu.id == menu_id)
        .filter(models.Submenu.id == submenu_id)
        .first()
    )
    return res


def create_submenu(menu_id: str, submenu: schemas.SubmenuBase, db: Session):
    submenu_db = models.Submenu(
        title=submenu.title,
        description=submenu.description,
        dishes_count=0,
        menu_id=menu_id,
    )
    db.add(submenu_db)
    db.commit()
    db.refresh(submenu_db)
    return submenu_db


def update_submenu(
    old_submenu: schemas.Submenu, new_submenu: schemas.SubmenuBase, db: Session
):
    old_submenu.title, old_submenu.description = (
        new_submenu.title,
        new_submenu.description,
    )
    db.add(old_submenu)
    db.commit()
    db.refresh(old_submenu)
    return old_submenu


def delete_submenu(menu_id: str, submenu_id: str, db: Session):
    submenu_db = get_submenu_by_id(menu_id, submenu_id, db)
    db.delete(submenu_db)
    db.commit()
