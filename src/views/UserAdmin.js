import React from 'react';
import { NavLink, Outlet } from 'react-router-dom';
import "../styles/UserAdmin.css";

const UserAdmin = () => {
    return (
        <div className="row gx-0">
            <div className="sidebar bg-success col-md-2 p-3">
                <a href="#" className="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-light text-decoration-none">
                    <span className="sidebar-title">Admin</span>
                </a>
                <hr />
                <ul className="sidebar-links nav flex-column mb-auto">
                    <NavLink to="/user/admin/map">Map</NavLink>
                    <NavLink to="/user/admin/report">Report</NavLink>
                    <NavLink to="/user/admin/edit">Edit</NavLink>
                    <NavLink to="/user/admin/List">List</NavLink>
                    <NavLink to="/user/admin/mod">Mod</NavLink>
                </ul>
                <hr />
                <div className="dropdown">
                    <a href="#" className="d-flex align-items-center link-light text-decoration-none dropdown-toggle" id="dropdownUser2" data-bs-toggle="dropdown" aria-expanded="false">
                        <strong>User's Email</strong>
                    </a>
                    <ul className="dropdown-menu bg-success text-small shadow" aria-labelledby="dropdownUser2">
                        <NavLink className="dropdown-item" to="/user/admin/profile">Profile</NavLink>
                        <NavLink className="dropdown-item" to="/user/admin/settings">Settings</NavLink>
                        <li><hr className="dropdown-divider" /></li>
                        <li><a className="dropdown-item" href="/login">Sign out</a></li>
                    </ul>
                </div>
            </div>
            <div className='col-md'>
                <Outlet />
            </div>
        </div>
    )
}

export default UserAdmin;