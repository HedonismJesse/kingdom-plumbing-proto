# Kingdom Plumbing — Production Feature Roadmap

> Priority matrix: **NEED** = must-have for any real deployment; **WANT** = competitive differentiator; **LATER** = future roadmap

---

## NEED (Must-Have — No Real Deployment Without These)

| # | Feature | Why Critical | Market Gap If Missing | Effort |
|---|---------|-------------|----------------------|--------|
| 1 | **Customer Portal** | Customers expect to book online, approve estimates, pay invoices, see ETA | Zero self-service = phone-only chaos, lost leads | Medium |
| 2 | **Dispatch Calendar** | Admin must see who's where, drag jobs to time slots, detect conflicts | Dispatch is 50% of the business. No calendar = whiteboard + phone calls | Medium |
| 3 | **Payment Processing** | Collecting payment in the field is the #1 success metric | Manual invoicing = 30+ day cash cycles, no card-on-file | Medium |
| 4 | **SMS Notifications** | "Tech arriving in 10 min", "Estimate ready for approval", "Job complete" | Modern customers live on text. Email is dead for field service | Low |
| 5 | **Estimate Approval Flow** | Customer views estimate online, approves with e-signature, auto-converts to job | Without approval gate, scope creep and disputes explode | Medium |
| 6 | **Offline Mobile Mode** | Techs work in basements, rural areas, dead zones | Data loss on every connectivity gap | High |
| 7 | **Push Notifications** | New assignment alerts, schedule change, urgent job ping | Techs miss updates = missed appointments = churn | Medium |
| 8 | **GPS / Route Optimization** | Driving is half the day. Optimize routes = save hours + fuel | Gas + labor wasted on backtracking | High |
| 9 | **Real Reporting Dashboard** | Revenue by tech, job profitability, callback rate, monthly trends | Owner flying blind = bad pricing, wrong tech assignments | Low |
| 10 | **Inventory / Parts Tracking** | "Did we use a ¾\" brass or ½\"?" Parts accountability = margin | Unbilled parts = 5-15% revenue leak | Medium |

---

## WANT (Competitive Differentiators — Close Deals)

| # | Feature | Why It Wins | Effort |
|---|---------|------------|--------|
| 11 | **Two-Way SMS Chat** | Customer replies "I'm running late" → tech sees it in app | Low |
| 12 | **QuickBooks / Xero Sync** | Double-entry kills bookkeepers. One-click sync = stickiness | Medium |
| 13 | **Photo Annotation** | Circle the leak, draw arrows, add measurements on photos before/after | Low |
| 14 | **Service Agreements / Recurring** | HVAC/plumbing live on maintenance contracts. Auto-generate recurring jobs | Medium |
| 15 | **Review / Reputation** | Auto-request Google/Yelp reviews after completed jobs | Low |
| 16 | **Form Builder / Checklists** | Safety inspections, pre-job checklists, compliance forms | Medium |
| 17 | **Equipment Tracking** | Serial numbers, warranties, service history per unit (water heater, furnace) | Medium |
| 18 | **Membership / Loyalty Programs** | Priority scheduling, discounted rates for recurring customers | Medium |
| 19 | **VoIP / Call Recording** | Track all customer calls, auto-log to job history | High |
| 20 | **AI Photo Estimating** | Customer uploads leak photo → auto-generate repair estimate | High |

---

## LATER (Roadmap — Year 2+)

| # | Feature | Notes |
|---|---------|-------|
| 21 | **Multi-location / Franchise** | Dispatch across branches, territory management |
| 22 | **Subcontractor Portal** | Outsource overflow jobs, track their completion |
| 23 | **Fleet Management** | Vehicle maintenance, GPS tracking, fuel logs |
| 24 | **AI Scheduling Agent** | Auto-optimize daily routes based on tech skills, location, urgency |
| 25 | **Customer Mobile App** | iOS/Android native app for booking, tracking, payments |
| 26 | **Integration Marketplace** | Zapier, Slack, HubSpot, Mailchimp connectors |
| 27 | **Advanced Analytics** | Predictive maintenance alerts, churn risk scoring |

---

## Current Kingdom Plumbing Status

| Feature | Status | Next Action |
|---------|--------|-------------|
| Clock In/Out | ✅ Backend + Mobile mockup | Add live running timer |
| Job List | ✅ Backend + Mobile mockup | — |
| Job Detail | ✅ Backend + Mobile mockup | Add photo gallery per job |
| Photo Upload | ✅ Backend + Mobile mockup | Wire to real camera |
| Document Storage | ✅ Backend + Mobile mockup | — |
| PIN Auth | ✅ Backend + Mobile mockup | Add login screen |
| Employee CRUD | ✅ Backend + Admin panel | — |
| Timesheets | ✅ Backend + Admin panel | Add date-range filtering |
| Customer CRM | ✅ Backend | Needs customer portal |
| Estimates | ✅ Backend | Needs approval flow |
| Invoices | ✅ Backend | Needs Stripe + customer pay link |
| Leads | ✅ Backend | Needs online booking form |
| **Customer Portal** | ❌ | **BUILD NOW** |
| **Dispatch Calendar** | ❌ | **BUILD NOW** |
| **Payment Processing** | ❌ | **BUILD NOW** |
| **SMS Notifications** | ❌ | **BUILD NOW** |
| **Reporting Dashboard** | ❌ | **BUILD NOW** |
| Offline Mode | ❌ | Roadmap |
| Push Notifications | ❌ | Roadmap |
| GPS / Routes | ❌ | Roadmap |
| Inventory | ❌ | Roadmap |
| QuickBooks Sync | ❌ | Roadmap |
| Photo Annotation | ❌ | Roadmap |
| Service Agreements | ❌ | Roadmap |
| Reviews | ❌ | Roadmap |
| Forms / Checklists | ❌ | Roadmap |
| Equipment Tracking | ❌ | Roadmap |
| VoIP | ❌ | Roadmap |
| AI Photo Estimating | ❌ | Roadmap |
