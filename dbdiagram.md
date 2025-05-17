enum UserPlanStatus {
  "active"
  "inactive"
  "pending"
  "suspended"
}

enum Role {
  "system"
  "host"
  "customer"
  "guest"
}


enum Status {
  "active"
  "inactive"
}

enum PaymentStatus {
  "not_paid"
  "pending"
  "paid"
}

enum SubscriptionStatus {
  "active"
  "inactive" 
}

enum ReportStatus {
  "new"
  "pending"
  "inprogress"
  "completed"
}

// Services User
Table Users {
  user_uuid uuid [pk]
  user_email string
  user_password string
  user_first_name string
  user_last_name string
  user_birthday string
  user_status Status
  user_native_language string
  user_active_key string
  user_role Role
  user_has_bill boolean
  user_onboarding boolean
  user_updated_at int
  user_created_at int
}


Table UserRefreshToken {
  user_uuid uuid
  refresh_token_used string
}



Table UserPlan {
  user_id uuid [pk]
  plan_id uuid
  userplan_status UserPlanStatus
}


Table Topic {
  topic_id uuid [pk]
  topic_name string
}

Table UserTopic {
  user_id uuid
  topic_array string
}


Table Plan {
  plan_id uuid
  plan_name string
  plan_title string
  plan_desc string
  plan_amount number
  plan_most_popular boolean
}


Table GroupSettings {
  groupsetting_id uuid
  groupsetting_value string
}

Table Settings {
  setting_id uuid
  groupsetting_id uuid
  setting_key string
  setting_value string
}


Table Payments {
  payment_id uuid
  transaction_id uuid
  paymentmethod_id uuid
  plan_name string
  amount number
  customer_name string
  customer_email string
  payment_status PaymentStatus
  payment_created_at string
  payment_updated_at string
}


Table PaymentMethod {
  paymentmethod_id uuid
  paymentmethod_name string
}


Table Subscriptions {
  sub_id  uuid
  customer_id uuid
  payment_id uuid
  sub_next_bill string // check neu ngay <= now thi lay ngay hien tai + plan. Neu next_bill > now => Cong them plan
  sub_started_date string
  sub_status SubscriptionStatus
}


Table Report {
  report_id uuid
  report_fullname string
  priority number
  report_reason string
  status ReportStatus
}


Ref: "Users"."user_uuid" < "UserRefreshToken"."user_uuid"

Ref: "Users"."user_uuid" < "UserTopic"."user_id"

Ref: "Topic"."topic_id" < "UserTopic"."topic_array"

Ref: "Plan"."plan_id" < "UserPlan"."plan_id"

Ref: "UserPlan"."user_id" < "Users"."user_uuid"

Ref: "GroupSettings"."groupsetting_id" < "Settings"."groupsetting_id"

Ref: "Payments"."paymentmethod_id" < "PaymentMethod"."paymentmethod_id"

Ref: "Subscriptions"."payment_id" < "Payments"."payment_id"