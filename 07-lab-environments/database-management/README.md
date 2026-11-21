# Study Guide: MySQL Data Management
> **Draft study guide ? exercise results and prior evidence are unavailable or have not been reverified. Treat existing details as study notes; rerun and sanitize before reporting results.**



This combined pathway covers MySQL Workbench/Sakila practice, database accounts and recovery, and IT asset tracker schema design. Detailed runbooks and SQL files remain separate supporting components.

## Skills Demonstrated

- Combine query, privilege, backup/restore, and schema-design workflows.
- Use sample or synthetic data.
- Compare evidence requirements across database exercises.

*Complete marked steps and record actual results before claiming hands-on completion.*

## Suggested sequence

1. [MySQL Workbench and Sakila](mysql-workbench-sakila-practice.md) — install, connect, inspect the sample schema, and run queries.
2. [MySQL Users, Privileges, Backup, and Restore](mysql-users-privileges-and-recovery.md) — use local-only lab accounts, test grants, back up, and validate restore.
3. [IT Asset Tracker Database Design](database-design-practice.md) — review the ERD and run the schema/constraint exercise.

## Supporting files

- SQL scripts: [`sakila_practice.sql`](sql/sakila_practice.sql), [`users_and_backup_exercise.sql`](sql/users_and_backup_exercise.sql), [`it_asset_tracker.sql`](sql/it_asset_tracker.sql), and [`cookie_bakery.sql`](sql/cookie_bakery.sql).
- Screenshots: [MySQL Workbench](images/01-workbench-between-query.png) and [database design diagrams](images/).

## Environment

Use one local MySQL installation with the Sakila sample database and the included synthetic exercises. Keep the service bound to localhost; never expose port 3306 to the public internet. Use dummy accounts and passwords only.

Record actual server and Workbench versions and results; no test results are implied by the SQL templates.


