# 🚀 API Pagination Cheat Sheet

Pagination = controlling how much data an API returns at once.
Two main strategies: **Limit & Offset** vs **Cursor-based**.
But first—know your data.

---

## 🔑 Deterministic vs Indeterministic Results

- **Deterministic** → Always returns same set on re-run. (_*idempotent read*_)
  - `ORDER BY id ASC`
- **Indeterministic** → Results can drift with ordering, new inserts, deletes, updates.
  - `WHERE name LIKE 'A%'`

👉 **Always enforce deterministic ordering** → use unique columns because pagination needs predictable ordering to avoid duplicates/missing rows.

- Example: (`id`, `timestamp + id`),

---

## 1️⃣ Limit & Offset Pagination

**Mechanics**

```sql
SELECT *
FROM users
ORDER BY id ASC
LIMIT 10 OFFSET 30;
```

**✅ Pros**

- Stateless → Only page_number and page_size (optional) is passed from the client.
- Random Access → Client can jump to any page (`page=123`).
- Limit → page_size
- Offset → (page_number - 1) \* page_size

**❌ Cons**

- Performance dips for deep pages → DB fetches + discards rows.
- Record drift possible with indeterministic queries (items shift between pages).

---

## 2️⃣ Cursor-based Pagination

**Mechanics**

```sql
-- If last seen id = 50
SELECT *
FROM users
WHERE id > 50
ORDER BY id ASC
LIMIT 10;
```

**✅ Pros**

- Stateful → Client must track the last seen `cursor` (next_key) and page_size(optional).
- Efficient for large datasets → avoids costly `OFFSET`.
- Stable results (no skipping/duplicates if ordered deterministically).
- Perfect for infinite scrolling or streaming feeds (social media, chats).

**❌ Cons**

- Sequential access only (no "jump to page 99").
- Query gets tricky when cursor is composite (e.g., `(created_at, id)` for uniqueness).

---

## ⚖️ Quick Comparison

| Feature                  | Limit & Offset    | Cursor-based                 |
| ------------------------ | ----------------- | ---------------------------- |
| Implementation           | ✅ Simple         | ❌ Complex                   |
| Performance (deep pages) | ❌ Slow           | ✅ Fast                      |
| Drift resistance         | ❌ Prone          | ✅ Strong (if deterministic) |
| Access                   | Random            | Sequential                   |
| State                    | Stateless         | Stateful (cursor needed)     |
| Best use case            | Dashboards, admin | Infinite scroll, feeds       |

---
