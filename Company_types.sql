BEGIN TRANSACTION;
CREATE TABLE Company_types (
        `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        `companyType`    TEXT,
        'description'  TEXT
    );
INSERT INTO `Company_types` VALUES (0,'S.A.','spółka akcyjna');
INSERT INTO `Company_types` VALUES (1,'sp. z o.o.','spółka z ograniczoną odpowiedzialnością');
INSERT INTO `Company_types` VALUES (2,'sp. j.','spółka jawna');
INSERT INTO `Company_types` VALUES (3,'sp.p.','spółka partnerska');
INSERT INTO `Company_types` VALUES (4,'sp. k.','spółka komandytowa');
INSERT INTO `Company_types` VALUES (5,'S.K.A.','spółka komandytowo-akcyjna');
CREATE INDEX "polls_choice_7aa0f6ee" ON "polls_choice" ("question_id");
CREATE INDEX "documents_upadlosc_f3af7fc2" ON "documents_upadlosc" ("colorCode_id");
CREATE INDEX "documents_legal_a643ae54" ON "documents_legal" ("adress_id_id");
CREATE INDEX "documents_legal_02869058" ON "documents_legal" ("companyType_id_id");
CREATE INDEX "documents_courts_a643ae54" ON "documents_courts" ("adress_id_id");
CREATE INDEX "documents_correspondencies_6ba603a3" ON "documents_correspondencies" ("contact_id_id");
CREATE INDEX "documents_correspondencies_3d60f6a7" ON "documents_correspondencies" ("correspondencyType_id_id");
CREATE INDEX "documents_correspondencies_39287bb7" ON "documents_correspondencies" ("client_id_id");
CREATE INDEX "documents_correspondencies_235b2128" ON "documents_correspondencies" ("mentionedClient_id_id");
CREATE INDEX "documents_correspondencies_1abca306" ON "documents_correspondencies" ("contactsGroup_id_id");
CREATE INDEX "documents_contacts_d8488902" ON "documents_contacts" ("court_id_id");
CREATE INDEX "documents_contacts_51ffeac5" ON "documents_contacts" ("legal_id_id");
CREATE INDEX "documents_contacts_4fc84bb3" ON "documents_contacts" ("baillif_id_id");
CREATE INDEX "documents_clients_382c1158" ON "documents_clients" ("folder_id_id");
CREATE INDEX "documents_bailiffs_a643ae54" ON "documents_bailiffs" ("adress_id_id");
CREATE INDEX "documents_bailiffs_02869058" ON "documents_bailiffs" ("companyType_id_id");
CREATE INDEX "documents_adresses_563cf480" ON "documents_adresses" ("country_id_id");
CREATE INDEX "django_session_de54fa62" ON "django_session" ("expire_date");
CREATE UNIQUE INDEX "django_content_type_app_label_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE INDEX "django_admin_log_e8701ad4" ON "django_admin_log" ("user_id");
CREATE INDEX "django_admin_log_417f1b1c" ON "django_admin_log" ("content_type_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_e8701ad4" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_8373b171" ON "auth_user_user_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_e8701ad4" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_0e939a4f" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_permission_content_type_id_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_417f1b1c" ON "auth_permission" ("content_type_id");
CREATE UNIQUE INDEX "auth_group_permissions_group_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_8373b171" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_group_permissions_0e939a4f" ON "auth_group_permissions" ("group_id");
CREATE INDEX "attachments_attachment_417f1b1c" ON "attachments_attachment" ("content_type_id");
CREATE INDEX "attachments_attachment_3700153c" ON "attachments_attachment" ("creator_id");
COMMIT;
