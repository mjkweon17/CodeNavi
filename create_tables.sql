CREATE TABLE `User` (
	`user_id`	INT	NOT NULL,
	`password`	VARCHAR(255)	NOT NULL,
	`is_active`	BOOL	NOT NULL	DEFAULT TRUE,
	`created_at`	DATETIME	NOT NULL,
	`Field`	VARCHAR(255)	NOT NULL,
	`Field2`	VARCHAR(255)	NOT NULL
);

CREATE TABLE `Lecture` (
	`lecture_id`	INT	NOT NULL,
	`is_active`	BOOL	NOT NULL	DEFAULT TRUE,
	`created_at`	DATETIME	NOT NULL,
	`language`	VARCHAR(255)	NOT NULL	DEFAULT 'korean',
	`title`	VARCHAR(255)	NOT NULL,
	`thumbnail`	VARCHAR(255)	NULL,
	`lecturer`	VARCHAR(255)	NOT NULL,
	`couse_hours`	VARCHAR(255)	NULL,
	`difficulty`	VARCHAR(255)	NULL,
	`company_id`	VARCHAR(255)	NOT NULL,
	`price`	VARCHAR(255)	NULL,
	`discount_rate`	VARCHAR(255)	NULL,
	`introduction`	TEXT	NULL
);

CREATE TABLE `Review` (
	`review_id`	INT	NOT NULL,
	`lecture_id`	INT	NOT NULL,
	`user_id`	INT	NOT NULL,
	`star`	INT	NOT NULL,
	`good_review`	TEXT	NOT NULL,
	`bad_review`	TEXT	NOT NULL,
	`is_active`	BOOL	NOT NULL	DEFAULT TRUE,
	`created_at`	DATETIME	NOT NULL
);

CREATE TABLE `STACK_CATEGORY` (
	`stack_category_id`	INT	NOT NULL,
	`parent_id`	INT	NULL,
	`Field`	INT	NOT NULL
);

CREATE TABLE `UserStack` (
	`user_stack_id`	INT	NOT NULL,
	`user_id`	INT	NOT NULL,
	`stack_category_id`	INT	NOT NULL
);

CREATE TABLE `LectureStack` (
	`lecture_stack_id`	INT	NOT NULL,
	`stack_category_id`	INT	NOT NULL,
	`lecture_id`	INT	NOT NULL
);

CREATE TABLE `Company` (
	`company_id`	INT	NOT NULL,
	`company_name`	VARCHAR(255)	NOT NULL
);

CREATE TABLE `Bookmark` (
	`bookmark_id`	INT	NOT NULL,
	`user_id`	INT	NOT NULL,
	`lecture_id`	INT	NOT NULL
);

CREATE TABLE `BOARD` (
	`board_id`	INT	NOT NULL,
	`user_id`	INT	NOT NULL,
	`title`	VARCHAR(255)	NOT NULL,
	`created_at`	DATETIME	NOT NULL,
	`is_active`	BOOL	NOT NULL	DEFAULT TRUE
);

ALTER TABLE `User` ADD CONSTRAINT `PK_USER` PRIMARY KEY (
	`user_id`
);

ALTER TABLE `Lecture` ADD CONSTRAINT `PK_LECTURE` PRIMARY KEY (
	`lecture_id`
);

ALTER TABLE `Review` ADD CONSTRAINT `PK_REVIEW` PRIMARY KEY (
	`review_id`
);

ALTER TABLE `STACK_CATEGORY` ADD CONSTRAINT `PK_STACK_CATEGORY` PRIMARY KEY (
	`stack_category_id`
);

ALTER TABLE `UserStack` ADD CONSTRAINT `PK_USERSTACK` PRIMARY KEY (
	`user_stack_id`
);

ALTER TABLE `LectureStack` ADD CONSTRAINT `PK_LECTURESTACK` PRIMARY KEY (
	`lecture_stack_id`
);

ALTER TABLE `Company` ADD CONSTRAINT `PK_COMPANY` PRIMARY KEY (
	`company_id`
);

ALTER TABLE `Bookmark` ADD CONSTRAINT `PK_BOOKMARK` PRIMARY KEY (
	`bookmark_id`
);

ALTER TABLE `BOARD` ADD CONSTRAINT `PK_BOARD` PRIMARY KEY (
	`board_id`
);

