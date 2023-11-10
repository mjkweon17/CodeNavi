CREATE TABLE `HKUser` (
	`user_id`	INT	AUTO_INCREMENT	NOT NULL,
	`password`	VARCHAR(255)	NOT NULL,
	`is_active`	BOOL	NOT NULL	DEFAULT TRUE,
	`created_at`	DATETIME	NOT NULL,
	`github_id`	VARCHAR(255)	NOT NULL,
	`blog_link`	VARCHAR(255)	NOT NULL,
    PRIMARY KEY (`user_id`)
);

CREATE TABLE `HKCompany` (
	`company_id`	INT	AUTO_INCREMENT	NOT NULL,
	`company_name`	VARCHAR(255)	NOT NULL,
    PRIMARY KEY (`company_id`)
);

CREATE TABLE `HKLecture` (
	`lecture_id`	INT	AUTO_INCREMENT	NOT NULL,
	`is_active`	BOOL	NOT NULL	DEFAULT TRUE,
	`created_at`	DATETIME	NOT NULL,
	`language`	VARCHAR(255)	NOT NULL	DEFAULT 'korean',
	`title`	VARCHAR(255)	NOT NULL,
	`thumbnail`	VARCHAR(255)	NULL,
	`lecturer`	VARCHAR(255)	NOT NULL,
	`course_hours`	VARCHAR(255)	NULL,
	`difficulty`	VARCHAR(255)	NULL,
	`company_id`	INT	NOT NULL,
	`price`	VARCHAR(255)	NULL,
	`discount_rate`	VARCHAR(255)	NULL,
	`introduction`	TEXT	NULL,
    PRIMARY KEY (`lecture_id`),
    FOREIGN KEY (`company_id`) REFERENCES `HKCompany` (`company_id`) ON UPDATE CASCADE
);

CREATE TABLE `HKReview` (
	`review_id`	INT	AUTO_INCREMENT	NOT NULL,
	`lecture_id`	INT	NOT NULL,
	`user_id`	INT	NOT NULL,
	`star`	INT	NOT NULL,
	`good_review`	TEXT	NOT NULL,
	`bad_review`	TEXT	NOT NULL,
	`is_active`	BOOL	NOT NULL	DEFAULT TRUE,
	`created_at`	DATETIME	NOT NULL,
    PRIMARY KEY (`review_id`),
    FOREIGN KEY (`lecture_id`) REFERENCES `HKLecture` (`lecture_id`) ON UPDATE CASCADE,
    FOREIGN KEY (`user_id`) REFERENCES `HKUser` (`user_id`) ON UPDATE CASCADE
);

CREATE TABLE `HKBookmark` (
	`bookmark_id`	INT	AUTO_INCREMENT	NOT NULL,
	`user_id`	INT	NOT NULL,
	`lecture_id`	INT	NOT NULL,
    PRIMARY KEY (`bookmark_id`),
    FOREIGN KEY (`user_id`) REFERENCES `HKUser` (`user_id`) ON UPDATE CASCADE,  
    FOREIGN KEY (`lecture_id`) REFERENCES `HKLecture` (`lecture_id`) ON UPDATE CASCADE
);

CREATE TABLE `HKSTACK_CATEGORY` (
	`stack_category_id`	INT	AUTO_INCREMENT	NOT NULL,
	`parent_id`	INT	NULL,
	`stack_name`	INT	NOT NULL,
    PRIMARY KEY (`stack_category_id`),
    FOREIGN KEY (`parent_id`) REFERENCES `HKSTACK_CATEGORY` (`stack_category_id`) ON UPDATE CASCADE
);

CREATE TABLE `HKLectureStack` (
	`lecture_stack_id`	INT	AUTO_INCREMENT	NOT NULL,
	`stack_category_id`	INT	NOT NULL,
	`lecture_id`	INT	NOT NULL,
    PRIMARY KEY (`lecture_stack_id`),
    FOREIGN KEY (`stack_category_id`) REFERENCES `HKSTACK_CATEGORY` (`stack_category_id`) ON UPDATE CASCADE,
    FOREIGN KEY (`lecture_id`) REFERENCES `HKLecture` (`lecture_id`) ON UPDATE CASCADE
);

CREATE TABLE `HKUserStack` (
	`user_stack_id`	INT	AUTO_INCREMENT	NOT NULL,
	`user_id`	INT	NOT NULL,
	`stack_category_id`	INT	NOT NULL,
    PRIMARY KEY (`user_stack_id`),
    FOREIGN KEY (`user_id`) REFERENCES `HKUser` (`user_id`) ON UPDATE CASCADE,
    FOREIGN KEY (`stack_category_id`) REFERENCES `HKSTACK_CATEGORY` (`stack_category_id`) ON UPDATE CASCADE
);

CREATE TABLE `HKBoard` (
	`board_id`	INT	AUTO_INCREMENT	NOT NULL,
	`user_id`	INT	NOT NULL,
	`title`	VARCHAR(255)	NOT NULL,
	`created_at`	DATETIME	NOT NULL,
	`is_active`	BOOL	NOT NULL	DEFAULT TRUE,
    `content`	TEXT	NOT NULL,
    PRIMARY KEY (`board_id`),
    FOREIGN KEY (`user_id`) REFERENCES `HKUser` (`user_id`) ON UPDATE CASCADE
);