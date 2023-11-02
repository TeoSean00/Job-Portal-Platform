import { decl } from "postcss";

declare type SidebarNavItem = {
  title: string;
  href: string;
  icon: React.ReactElement;
};

declare type User = {
  staff_id: number;
  fname: string;
  lname: string;
  dept: string;
  email: string;
  phone: string;
  biz_address: string;
  sys_role: string;
};

declare type Skill = { value: string; label: string };

declare type Department = { value: string; label: string };

declare type RoleDetail = {
  role_id: number;
  role_name: string;
  role_description: string;
  role_status: string;
};

declare type SkillDetail = {
  skill_status: string;
  skill_name: string;
  skill_id: number;
};

declare type RoleSkillId = {
  role_id: number;
  skill_id: number;
};

declare type RoleSkillAPIResponse = {
  role_skills: RoleSkillId[];
};

declare type SkillAPIResponse = {
  skill_status: string;
  skill_name: string;
  skill_id: number;
};

declare type StaffIdAPIResponse = {
  staff_id: number;
  fname: string;
  lname: string;
  dept: string;
  email: string;
  phone: string;
  biz_address: string;
  sys_role: string;
};

declare type AllSkillAPIResponse = {
  skills: SkillDetail[];
};

declare type FetcherOptions = RequestInit;

declare type RoleAPIResponse = {
  role_details: RoleDetail[];
};

declare type RoleFormProps = {
  departments: Department[];
  roles: RoleDetail[];
  allSkills: SkillAPIResponse[];
};

declare type UpdateFormProps = {
  departments: Department[];
  roles: RoleDetail[];
  allSkills: SkillAPIResponse[];
  roleToUpdateData: RoleListing;
};

declare type RoleFormValues = {
  roleName: string;
  listingId: string;
  roleDescription: string;
  roleManager: string;
  location: string;
  departments: string;
  skills: { value: string }[];
  startDate: Date;
};

declare type RoleSkill = {
  skill_id: number;
  skill_name: string;
  skill_status: string;
};

declare type RoleItem = {
  role_id: number;
  role_name: string;
  role_desc: string;
  role_status: string;
  skills: RoleSkill[];
};

declare type SpecificRoleInfo = {
  role_name: string;
  role_desc: string;
  role_status: string;
  skills: RoleSkill[];
  role_department: string;
  role_location: string;
  role_listing_desc: string;
};

declare type SkillMatchType = {
  active: RoleSkill[];
  in_progress: RoleSkill[];
  unverified: RoleSkill[];
};
export type Option = {
  label: string;
  value: string;
  icon?: React.ComponentType<{ className?: string }>;
};

export type DatePickerWithPresetsProps = {
  className?: string;
  value: Date;
  onChange: (selectedDate: Date) => void;
};

export interface DataTableSearchableColumn<TData> {
  id: keyof TData;
  title: string;
}

export interface DataTableFilterableColumn<TData>
  extends DataTableSearchableColumn<TData> {
  options: Option[];
}

export type TRoleApplicantDetails = {
  biz_address: string;
  dept: string;
  email: string;
  fname: string;
  lname: string;
  phone: string;
  role_app_id: number;
  role_app_status: string;
  role_app_ts_create: string;
  role_listing_id: number;
  staff_id: number;
  sys_role: string;
};

export type TRoleDetails = {
  role_id: number;
  role_name: string;
  role_description: string;
  role_status: string;
};

declare type RoleListing = {
  role_listing_id: number;
  role_id: number;
  role_listing_desc: string;
  role_listing_source: number;
  role_listing_open: string;
  role_listing_close: string;
  role_listing_hide: null | string;
  role_listing_creator: number;
  role_listing_ts_create: string;
  role_listing_updater: null | number;
  role_listing_ts_update: null | string;
  role_department: string;
  role_location: string;
};

declare type RoleToUpdateData = {
  role_listing: {
    role_listing: RoleListing;
  };
};
