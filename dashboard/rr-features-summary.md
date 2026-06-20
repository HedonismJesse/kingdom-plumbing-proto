# R&R Home Repairs — Feature Summary Table

> Reference: Replit export at `ReplitExport-jessejenkins2nd/Free-Today/artifacts/rr-worker-app/`

---

## 1. Mobile App — Worker / Technician View

| Feature | Screen | Description |
|---------|--------|-------------|
| **Clock In/Out** | Clock | One-tap clock in/out with live running timer (HH:MM:SS) |
| **Today's Hours** | Clock | Hours worked today with session count |
| **Time Log** | Clock | Scrollable list of today's entries (in → out, duration) |
| **Job List** | Jobs | Current + upcoming jobs with status color coding |
| **Job Detail** | Jobs | Customer name, address, service type, notes, est. total/time |
| **Directions** | Jobs | One-tap open address in maps app |
| **Job Photos** | Jobs | View photos tied to a job (Before / After / General) |
| **Add Note** | Jobs | Text note entry for job log |
| **Mark Complete** | Jobs | Status change to completed |
| **Customer Signature** | Jobs | Signature capture pad for sign-off |
| **Photo Grid** | Photos | 3-column masonry grid of all uploaded photos |
| **Photo Categories** | Photos | Filter/label: Before, After, Plumbing, Electrical, HVAC, etc. |
| **Camera Upload** | Photos | Take photo → add title → pick category → save |
| **Library Upload** | Photos | Select from phone gallery → add metadata → save |
| **Document List** | Documents | Filterable list: All / Paystubs / Tax Docs / Other |
| **Paystub Viewer** | Documents | Period range, amount, open PDF via URL |
| **Tax Doc Viewer** | Documents | W-2, 1099, etc. with tax year labeling |
| **External Doc Link** | Documents | Links to Drive/Dropbox-hosted files |
| **Profile Card** | Profile | Avatar (initials), name, role badge |
| **Contact Info** | Profile | Phone + email display |
| **Change PIN** | Profile | 6-digit numpad: current → new → confirm flow |
| **Sign Out** | Profile | Logout with confirmation dialog |
| **Team Directory** | Team | All workers with weekly hours, role badges |
| **Call Teammate** | Team | One-tap dial from team list |
| **Email Teammate** | Team | One-tap compose from team list |
| **Schedule/Appointments** | Schedule | Pending / Approved / Declined / Completed filter |
| **Approve Job** | Schedule | Worker accepts assigned appointment |
| **Decline Job** | Schedule | Worker rejects with status update |
| **Pull-to-Refresh** | All | Standard iOS-style refresh on all list screens |
| **Haptic Feedback** | All | Light/Medium impact on all button presses |

---

## 2. Mobile App — Admin View

| Feature | Screen | Description |
|---------|--------|-------------|
| **Admin Gate** | Admin | Role-based redirect (non-admin → clock screen) |
| **Timesheets** | Admin | Date range picker (From/To), grouped by worker |
| **Weekly Summary** | Admin | Per-worker: sessions count + total hours |
| **Daily Entries** | Admin | Clock-in → clock-out timestamps per worker |
| **Add Worker** | Admin | Form: name, role (worker/admin), PIN, phone, email |
| **Role Toggle** | Admin | Worker vs Admin assignment at creation |
| **Upload Document** | Admin | Select worker → type (paystub/tax/other) → title → URL → date range |
| **Worker Pills** | Admin | Horizontal scroll of worker names for doc assignment |

---

## 3. Website / Landing Page

| Feature | Page | Description |
|---------|------|-------------|
| **Expo Go Preview** | Landing | QR code + deep link for mobile preview |
| **Store Buttons** | Landing | App Store + Google Play download links |
| **Platform Detection** | Landing | Auto-detects iOS/Android for correct store button |
| **Auto-Redirect** | Landing | Mobile visitors auto-redirect to `exps://` deep link |
| **Dark Mode** | Landing | `prefers-color-scheme` responsive styling |

---

## 4. Cross-Cutting System Features

| Feature | Scope | Description |
|---------|-------|-------------|
| **PIN Authentication** | App-wide | 4–8 digit PIN login per worker |
| **Role-Based Access** | App-wide | Worker vs Admin route guards |
| **TanStack Query** | Data | Caching, refetching, optimistic updates |
| **API Client** | Data | Typed React hooks per entity (useListX, useCreateX, etc.) |
| **Safe Area Insets** | UI | iOS notch/home indicator compensation |
| **Theme Colors** | UI | Centralized color tokens (primary, success, danger, etc.) |
| **Plus Jakarta Sans** | Typography | Custom font family throughout |

---

## 5. Data Entities

| Entity | Worker Actions | Admin Actions |
|--------|---------------|---------------|
| **Worker** | View self | Create, view all, assign hours |
| **Time Entry** | Clock in/out, view self | View all, filter by date, group by worker |
| **Appointment** | Approve/decline, view assigned | (implied: create, assign) |
| **Document** | View own, filter by type | Upload to any worker, set period |
| **Photo** | Upload, categorize, view own | (implied: view all) |
| **Gallery** | Browse grid | — |

---

## 6. Kingdom Plumbing — Gap Analysis

| R&R Feature | Kingdom Status | Priority |
|-------------|---------------|----------|
| Clock In/Out | ✅ Basic time API exists | — |
| Live Timer | ❌ Not in UI | Medium |
| Today's Hours | ❌ Not in UI | Medium |
| Time Log | ❌ Not in UI | Medium |
| Job List | ✅ Dashboard Active Jobs | — |
| Job Detail | ✅ Mobile mockup has it | — |
| Directions | ❌ Not wired | Low |
| Job Photos | ❌ No photo model | High |
| Add Note | ❌ No note field on job | Medium |
| Mark Complete | ✅ Workflow action exists | — |
| Customer Signature | ❌ No signature model | Low |
| Photo Grid | ❌ No photo model | High |
| Photo Upload | ❌ No upload endpoint | High |
| Photo Categories | ❌ No category enum | Medium |
| Documents | ❌ No document model | High |
| Paystubs | ❌ No document model | High |
| Tax Docs | ❌ No document model | Medium |
| Profile | ❌ Static mockup only | Medium |
| Change PIN | ❌ No PIN auth | Medium |
| Team Directory | ❌ No team view | Low |
| Schedule/Appointments | ❌ No appointment model | Medium |
| Approve/Decline Job | ❌ No appointment model | Medium |
| Admin Timesheets | ❌ No admin panel | Medium |
| Add Worker | ✅ API exists, no admin UI | Medium |
| Upload Document | ❌ No document API | High |
| PIN Auth | ❌ No auth system | High |
| Role-Based Access | ❌ No roles on employee | High |
